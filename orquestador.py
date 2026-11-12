"""Ensamblado del orquestador con la configuración del entorno (.env): corpus + modelos + web + grafo.

Lo usan el CLI (`analizar.py`) y el notebook de la demo. Los tests arman el grafo directamente
con `graph.build_graph` y modelos guionados.
"""

from langchain_core.runnables import RunnableConfig
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.graph.state import CompiledStateGraph

from busqueda_web import buscador_desde_entorno
from config import DDSettings, dd_settings_from_env
from corpus import Corpus
from graph import Modelos, build_graph
from llm import get_chat_model, settings_from_env
from state import serializador


def crear_orquestador(settings: DDSettings | None = None, modelos: Modelos | None = None) -> tuple[CompiledStateGraph, Corpus, DDSettings]:
    """Grafo compilado con checkpointer en memoria (permite inspeccionar el historial de estados).

    Lanza ValidationError si la configuración es inválida (por ejemplo, falta la API key).
    """
    settings = settings or dd_settings_from_env()
    corpus = Corpus.desde_directorio(settings.data_dir)
    reintentos = 0
    if modelos is None:
        llm = settings_from_env()  # valida provider y API key
        especialistas = get_chat_model()
        supervisor = get_chat_model(model=settings.modelo_supervisor) if settings.modelo_supervisor else None
        modelos, reintentos = Modelos.mismo(especialistas, supervisor), llm.max_retries
    grafo = build_graph(
        modelos,
        corpus,
        settings,
        buscador_web=buscador_desde_entorno(),
        checkpointer=InMemorySaver(serde=serializador()),
        reintentos_llm=reintentos,
    )
    return grafo, corpus, settings


def config_analisis(thread_id: str, settings: DDSettings) -> RunnableConfig:
    """thread_id identifica el análisis; recursion_limit es el techo duro de super-pasos."""
    return {"configurable": {"thread_id": thread_id}, "recursion_limit": settings.recursion_limit}
