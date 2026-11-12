"""CLI: corre una due diligence completa y guarda el informe y la traza (requiere la API key del LLM).

Uso:
    python analizar.py --startup vozactiva
    python analizar.py --startup contralia --pedido "¿Aguanta el margen si el uso de LLM se duplica?"
    python analizar.py --listar

Salidas: informes/<startup>.md (informe con la recomendación preliminar) y trazas/<startup>.json
(recorrido del grafo, aportes por agente, parcelas finales y llamadas/tokens por agente).
"""

import argparse
import asyncio
import logging
import sys
import uuid

from dotenv import load_dotenv
from pydantic import ValidationError

from config import dd_settings_from_env, describir_error_config
from corpus import Corpus
from llm import describir_error_del_proveedor, es_error_del_proveedor
from logging_setup import configurar_logging
from orquestador import config_analisis, crear_orquestador
from tracing import analizar

PEDIDO_POR_DEFECTO = (
    "Hacé la due diligence de {nombre} para el comité de inversión: verificá las métricas del data room, "
    "calculá el costo real de los LLM y los unit economics, y marcá los riesgos que la startup no muestra."
)


async def main() -> int:
    parser = argparse.ArgumentParser(description="Due diligence multi-agente de startups de IA")
    parser.add_argument("--startup", help="id de la startup (carpeta en data/startups)")
    parser.add_argument("--pedido", help="pedido del usuario (por defecto, una due diligence completa)")
    parser.add_argument("--listar", action="store_true", help="lista las startups con data room")
    parser.add_argument("-v", "--verbose", action="store_true", help="muestra los logs de cada agente")
    args = parser.parse_args()

    load_dotenv()
    configurar_logging(logging.INFO if args.verbose else logging.WARNING)
    try:
        settings = dd_settings_from_env()
    except ValidationError as exc:
        print(describir_error_config(exc), file=sys.stderr)
        return 2

    # Listar y validar la startup no necesita API key: se resuelve antes de crear los modelos.
    startups = Corpus.desde_directorio(settings.data_dir).startups
    if args.listar or not args.startup:
        print("Startups disponibles: " + ", ".join(f"{k} ({v})" for k, v in startups.items()))
        return 0 if args.listar else 2
    if args.startup not in startups:
        print(f"No existe la startup '{args.startup}'. Opciones: {', '.join(startups)}", file=sys.stderr)
        return 2

    try:
        grafo, corpus, settings = crear_orquestador(settings)
    except ValidationError as exc:
        print(describir_error_config(exc), file=sys.stderr)
        return 2

    nombre = corpus.startups[args.startup]
    pedido = args.pedido or PEDIDO_POR_DEFECTO.format(nombre=nombre)
    print(f"Due diligence de {nombre}\nPedido: {pedido}\n")
    try:
        resultado = await analizar(grafo, args.startup, pedido, config_analisis(f"{args.startup}-{uuid.uuid4().hex[:8]}", settings))
    except Exception as exc:
        if es_error_del_proveedor(exc):
            print(describir_error_del_proveedor(exc), file=sys.stderr)
            return 1
        raise

    ruta_informe, ruta_traza = resultado.guardar(settings.informes_dir, settings.trazas_dir)
    uso = resultado.uso_llm["total"]
    print(f"\nRecomendación preliminar: {resultado.recomendacion}")
    print(f"Llamadas al LLM: {uso['llamadas']} · tokens: {uso['tokens_entrada']} de entrada, {uso['tokens_salida']} de salida · {resultado.latencia_s} s")
    if ruta_informe:
        print(f"Informe: {ruta_informe}")
    print(f"Traza: {ruta_traza}")
    return 0 if resultado.error is None else 1


if __name__ == "__main__":
    sys.exit(asyncio.run(main()))
