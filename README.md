# 🤖 Q&A System with PDF/TXT Support using Google Gemini + LlamaIndex

Welcome to the **Q&A System**, an intelligent document-questioning app powered by **Google Gemini**, **LlamaIndex**, and **Streamlit**.

🚀 **Live App**:  
🔗 [Click here to try the app](https://q-asystem-4ahiik5qduwngmn3mhcsbx.streamlit.app/)

---

## 📌 What does the app do?

This application allows users to:
- 📄 Upload a **PDF** or **TXT** document
- ❓ Ask any natural language question about the content
- 🤖 Get **accurate answers** extracted from the document using **Gemini LLM and Embeddings**

Whether it's a research paper, contract, or lecture notes — this system intelligently retrieves and responds using **LLM-powered document understanding**.

---

## 💡 Key Features

- ✅ **Supports both PDF and TXT file types**
- 🔍 **Information Retrieval** using LlamaIndex
- 🧠 **Embedding and Answering** with Google Gemini (`embedding-001` + Gemini-pro)
- ⚙️ Modular codebase with:
  - `data_ingestion.py` – handles document parsing
  - `embedding.py` – processes the document and builds the index
  - `model_api.py` – loads LLM
  - `exception.py` and `logger.py` – for robust error logging and tracing
- 📊 Clean and simple **Streamlit UI**

---

## 🧪 Tech Stack

| Tool/Library        | Purpose                             |
|---------------------|-------------------------------------|
| **Google GenerativeAI (Gemini)** | LLM and Embedding Models |
| **LlamaIndex**       | Vector Index and Query Engine       |
| **PyPDF**            | PDF Parsing                         |
| **Streamlit**        | Frontend Web Interface              |
| **Python-dotenv**    | Environment Configuration           |
| **Custom Logging**   | Logging and Error Handling          |

---

## 🖼️ UI Preview

![App Folder Structure Preview](https://github.com/MazenAhmedAbdalmohsen/Q-A_System/blob/master/docs/app_ui.png)  
<sup>📂 Screenshot from GitHub project structure</sup>

---

## 🧰 Installation & Usage

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/MazenAhmedAbdalmohsen/Q-A_System.git
cd Q-A_System
