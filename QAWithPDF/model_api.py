import os
import sys
from dotenv import load_dotenv
from llama_index.llms.gemini import Gemini
import google.generativeai as genai
from exception import customexception
from logger import logging

# Load environment variables
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Configure Gemini API
genai.configure(api_key=GOOGLE_API_KEY)


def load_model():
    """
    Loads the Gemini-Pro model using the provided API key.

    Returns:
        An initialized Gemini model instance.
    """
    try:
        logging.info("🔧 Initializing Gemini LLM model...")
        model = Gemini(models="gemini-pro", api_key=GOOGLE_API_KEY)
        logging.info("✅ Gemini model loaded successfully.")
        return model
    except Exception as e:
        logging.error("❌ Failed to load Gemini model.")
        raise customexception(e, sys)
