from PyPDF2 import PdfReader
from langchain_text_splitters import CharacterTextSplitter
from  langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS

def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text

def get_text_chunks(text):
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=500,
        chunk_overlap=100,
        length_function=len
    )
    chunks = text_splitter.split_text(text)
    print("Chunking Done")
    return chunks

def get_vector_store(text_chunks):
    # embedding_model = HuggingFaceInstructEmbeddings(model_name="hkunlp/instructor-xl", show_progress=True)
    embeddings = GoogleGenerativeAIEmbeddings(model="models/text-embedding-004")
    vector_store = FAISS.from_texts(texts=text_chunks, embedding=embeddings)
    print("Done")
    return vector_store