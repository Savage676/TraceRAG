import streamlit as st
from src.document_loader import count_pdf_pages, extract_pdf_pages
from src.text_splitter import split_pages


st.title("TraceRAG")
st.caption("Traceable document question answering with RAG")

uploaded_files = st.file_uploader(
    "Upload PDF document",
    type=["pdf"],
    accept_multiple_files=True,
)

all_chunks = []

if uploaded_files:
    st.success(f"Uploaded: {len(uploaded_files)} document(s).")

    for uploaded_file in uploaded_files:
        pdf_bytes = uploaded_file.getvalue()
        page_count = count_pdf_pages(pdf_bytes)

        pages = extract_pdf_pages(
            pdf_bytes,
            uploaded_file.name,
        )

        st.write(f"- {uploaded_file.name}: {page_count} page(s)")
        st.write(f"Extracted text from {len(pages)} page(s).")

        if pages:
            chunks = split_pages(pages,chunk_size=200,chunk_overlap=50,)
            all_chunks.extend(chunks)

            st.write(
                f"Document was split into "
                f"{len(chunks)} chunk(s)."
            )

            for chunk in chunks:
                label = (
                    f"Page {chunk['page']} · "
                    f"Chunk {chunk['chunk_id'] + 1}"
                )
                with st.expander(label):
                    st.write(chunk["text"])
                    st.caption(f"Source: {chunk['source']}")
            
        else:
            st.warning(
                f"No extractable text found in {uploaded_file.name}."
            )

    st.success(
        f"Created {len(all_chunks)} chunk(s) "
        f"from all uploaded documents."
    )

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

