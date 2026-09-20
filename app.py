import streamlit as st
from src.document_loader import count_pdf_pages, extract_page_pages

st.title("TraceRAG")
st.caption("Traceable document question answering with RAG")

uploaded_files = st.file_uploader(
    "Upload PDF document",
    type=["pdf"],
    accept_multiple_files=True,
)

if uploaded_files:
    st.success(f"Uploaded: {len(uploaded_files)} document(s).")

    for uploaded_file in uploaded_files:
        pdf_bytes = uploaded_file.getvalue()
        page_count = count_pdf_pages(pdf_bytes)
        pages = extract_page_pages(pdf_bytes,uploaded_file.name)

        st.write(f"-{uploaded_file.name}: {page_count} page(s)")
        st.write(pages[0]["text"][:500])
        st.caption(f"Source: {pages[0]['source']}, Page {pages[0]['page']}")

question = st.text_input(
    "Ask a question",
    placeholder="What would you like to know about these documents?",
)

ask_clicked = st.button("Ask",type="primary")

if ask_clicked:
    if not uploaded_files:
        st.warning("Please upload at least one PDF document.")
    elif not question.strip():
        st.warning("please enter a question")
    else:
        st.success("The request is ready to be processed.")
        st.write(f"Your question: {question}")


