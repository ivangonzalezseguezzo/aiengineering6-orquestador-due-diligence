"""Genera el diagrama del grafo para el README: docs/grafo.mmd (Mermaid, se genera localmente).

No llama al LLM: arma el grafo con un modelo de mentira, porque la topología no depende del modelo.
GitHub renderiza el bloque Mermaid del README directamente, así que no hace falta una imagen.

Opcional: `--png` genera docs/grafo.png con `draw_mermaid_png()`. Ojo: ese método ENVÍA el
diagrama al servicio público mermaid.ink para renderizarlo; por eso no se hace por defecto.

Uso:
    python dibujar_grafo.py          # docs/grafo.mmd + diagrama ASCII en consola
    python dibujar_grafo.py --png    # además docs/grafo.png (usa mermaid.ink)
"""

import argparse
import sys

from langchain_core.language_models.fake_chat_models import FakeListChatModel

from config import BASE_DIR, DDSettings
from corpus import Corpus
from graph import Modelos, build_graph


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--png", action="store_true", help="genera docs/grafo.png usando el servicio público mermaid.ink")
    args = parser.parse_args()

    settings = DDSettings()
    grafo = build_graph(Modelos.mismo(FakeListChatModel(responses=["-"])), Corpus.desde_directorio(settings.data_dir), settings)
    docs = BASE_DIR / "docs"
    docs.mkdir(exist_ok=True)
    mermaid = grafo.get_graph().draw_mermaid()
    (docs / "grafo.mmd").write_text(mermaid, encoding="utf-8")
    print(mermaid)
    try:
        print(grafo.get_graph().draw_ascii())
    except ImportError:
        print("(para el diagrama ASCII instalá grandalf)")
    if args.png:
        (docs / "grafo.png").write_bytes(grafo.get_graph().draw_mermaid_png())
        print(f"PNG: {docs / 'grafo.png'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
