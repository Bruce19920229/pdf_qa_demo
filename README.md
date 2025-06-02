# 🤖 PDF Question Answering App

A ChatGPT-powered PDF question answering system using LangChain, Streamlit, and OpenAI GPT-4-turbo.

## 💡 Features

- 📄 Upload any PDF file and extract full content
- ❓ Ask questions about the uploaded PDF
- 🧠 Uses GPT-4-turbo for accurate answers
- 🧷 Embeds PDF content using Chroma vector store
- 🔎 Supports long-document semantic search with LangChain
- 🖥️ Web interface via Streamlit

## 🚀 How to Run Locally

1. **Clone the repository**:

```bash
git clone https://github.com/your-username/pdf-qa-demo.git
cd pdf-qa-demo
```

2. **Install dependencies**:

```bash
pip install -r requirements.txt
```

3. **Add your OpenAI API key**:

Create a `.env` file in the project root:

```
OPENAI_API_KEY=your-api-key-here
```

4. **Start the Streamlit app**:

```bash
streamlit run main.py
```

Then open in browser: `http://localhost:8501`

## 📁 Project Structure

```
pdf_qa_demo/
│
├── main.py              # Streamlit web interface
├── qa_chain.py          # LangChain QA pipeline logic
├── pdf_tool.py          # PDF text extraction module
├── .streamlit/config.toml  # Streamlit config
├── requirements.txt     # Python dependencies
├── .env                 # OpenAI API key (not uploaded)
└── README.md            # Project instructions
```

## 🔐 Environment Variables

This app requires the following key in `.env`:

```
OPENAI_API_KEY=your_openai_key
```

## 📦 Dependencies

Key dependencies include:

- `langchain`
- `langchain-openai`
- `chromadb`
- `streamlit`
- `python-dotenv`
- `PyMuPDF` (for PDF reading)

Install them with:

```bash
pip install -r requirements.txt
```

## 🧪 Example

Upload a file like:

```
The_Little_Prince.pdf
```

Ask:
```
what is the story?
```

🧠 The app will search the document and respond using GPT-4-turbo.

## 📄 License

MIT License
