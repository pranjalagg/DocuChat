import streamlit as st
from dotenv import load_dotenv
from utils import get_pdf_text, get_text_chunks, get_vector_store

def main():
    st.set_page_config(page_title="DocuChat: Chat With Your PDFs", page_icon=":boooks:", layout="wide", initial_sidebar_state="auto")
    st.header("DocuChat: Chat With Your PDFs")
    st.text_input("Ask a question about your PDF(s)")

    with st.sidebar:
        st.subheader("Your Documents")
        pdf_docs = st.file_uploader("Upload PDFs and click on 'Process'", type=["pdf"], accept_multiple_files=True)
        if st.button("Process"):
            with st.spinner("Processing"):
                # get text from pdf
                raw_text = get_pdf_text(pdf_docs)

                # chunking
                text_chunks = get_text_chunks(raw_text)

                # vector store
                vector_store = get_vector_store(text_chunks)

if __name__ == "__main__":
    load_dotenv()
    main()