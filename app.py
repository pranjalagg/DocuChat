import streamlit as st
from dotenv import load_dotenv
from utils import get_pdf_text, get_text_chunks, get_vector_store, get_conversation_chain

def main():
    if "conversations" not in st.session_state:
        st.session_state.conversations = None
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

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

                # create conversation chain
                st.session_state.conversation = get_conversation_chain(vector_store)
    
    for message in st.session_state.chat_history:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Accept user input
    if user_question := st.chat_input("Your question"):
        with st.chat_message("user"):
            st.markdown(user_question)
        st.session_state.chat_history.append({"role": "user", "content": user_question})
        
        response = st.session_state.conversation({"question": user_question})
        st.session_state.chat_history.append({"role": "assistant", "content": response["answer"]})
        with st.chat_message("assistant"):
            st.markdown(response["answer"])
        # st.write(response)
    

if __name__ == "__main__":
    load_dotenv()
    main()