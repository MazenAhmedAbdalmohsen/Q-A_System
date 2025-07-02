from llama_index.core import VectorStoreIndex
from llama_index.core.settings import Settings
from llama_index.embeddings.gemini import GeminiEmbedding

from QAWithPDF.data_ingestion import load_data_from_pdf, load_data_from_txt
from QAWithPDF.model_api import load_model

import sys
from exception import customexception
from logger import logging


def download_gemini_embedding(model, document):
    """
    Initializes Gemini Embedding and returns a query engine 
    based on a VectorStoreIndex built from the given document.

    Args:
        model: The LLM model to use.
        document: The preprocessed document for embedding.

    Returns:
        A query engine instance for querying the embedded document.
    """
    try:
        logging.info("Initializing Gemini embedding model...")
        gemini_embed_model = GeminiEmbedding(model_name="models/embedding-001")

        logging.info("Configuring llama_index Settings...")
        # Set global defaults
        Settings.llm = model
        Settings.embed_model = gemini_embed_model
        Settings.chunk_size = 800
        Settings.chunk_overlap = 20

        logging.info("Building VectorStoreIndex from documents...")
        index = VectorStoreIndex.from_documents(document)

        logging.info("Persisting storage context...")
        index.storage_context.persist()

        logging.info("Creating query engine from index...")
        query_engine = index.as_query_engine()

        return query_engine

    except Exception as e:
        logging.error("❌ An error occurred while initializing embeddings.")
        raise customexception(e, sys)
