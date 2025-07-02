import sys
from llama_index.core import Document
from llama_index.core import SimpleDirectoryReader
from exception import customexception
from logger import logging


def load_data_from_pdf(data):
    """
    Load documents from the /Data directory for PDFs.
    """
    try:
        logging.info("📥 Loading PDF document(s)...")
        reader = SimpleDirectoryReader("Data")
        documents = reader.load_data()
        logging.info("✅ PDF documents loaded successfully.")
        return documents
    except Exception as e:
        logging.error("❌ Failed to load PDF document(s).")
        raise customexception(e, sys)


def load_data_from_txt(file):
    """
    Read content from uploaded TXT file and wrap in a Document.

    Args:
        file: Uploaded file object (.txt)

    Returns:
        List containing one Document.
    """
    try:
        logging.info("📥 Loading TXT document...")
        text = file.read().decode("utf-8")
        document = Document(text=text)
        logging.info("✅ TXT document loaded successfully.")
        return [document]
    except Exception as e:
        logging.error("❌ Failed to load TXT document.")
        raise customexception(e, sys)
