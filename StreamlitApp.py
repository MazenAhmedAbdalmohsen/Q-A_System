import streamlit as st
from QAWithPDF.data_ingestion import load_data_from_pdf, load_data_from_txt
from QAWithPDF.embedding import download_gemini_embedding
from QAWithPDF.model_api import load_model
from exception import customexception
from logger import logging


def main():
    st.set_page_config("QA with Documents", layout="centered")
    st.title("📄 QA with Documents")
    st.markdown("Upload a PDF or TXT file and ask questions based on its content.")

    uploaded_file = st.file_uploader("Upload your document (PDF or TXT)", type=["pdf", "txt"])
    user_question = st.text_input("💬 Ask your question:")

    if st.button("🚀 Submit & Process"):
        if uploaded_file is None or not user_question:
            st.warning("⚠️ Please upload a document and enter a question.")
            return

        with st.spinner("🔄 Processing your document and generating an answer..."):
            try:
                # Load document based on file type
                if uploaded_file.name.endswith(".pdf"):
                    documents = load_data_from_pdf(uploaded_file)
                elif uploaded_file.name.endswith(".txt"):
                    documents = load_data_from_txt(uploaded_file)
                else:
                    st.error("❌ Unsupported file type.")
                    return

                model = load_model()
                query_engine = download_gemini_embedding(model, documents)
                response = query_engine.query(user_question)

                st.success("✅ Answer generated:")
                st.write(response.response)

            except customexception as ce:
                st.error(f"❌ An error occurred: {str(ce)}")
                logging.error(str(ce))
            except Exception as e:
                st.error(f"❌ Unexpected error: {str(e)}")
                logging.exception("Unexpected error occurred.")


if __name__ == "__main__":
    main()
