import streamlit as st

def main():
    st.set_page_config(page_title="DocuChat: Chat With Your PDFs", page_icon=":boooks:", layout="wide", initial_sidebar_state="auto")
    st.header("DocuChat: Chat With Your PDFs")
    st.text_input("Ask a question about your PDF(s)")

    with st.sidebar:
        st.subheader("Your Documents")
        st.file_uploader("Upload PDFs and click on 'Process'", type=["pdf"], accept_multiple_files=True)
        st.button("Process")
    
if __name__ == "__main__":
    main()