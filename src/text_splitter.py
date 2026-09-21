def split_text(
        text: str,
        chunk_size: int = 500,
        chunk_overlap: int = 80,) -> list[str]:

    if chunk_overlap >= chunk_size:
        raise ValueError("chunk_overlap must be smaller than chunk_size.")

  
    chunks = []
    step_size = chunk_size - chunk_overlap

    for start in range(0,len(text),step_size):
        end = start + chunk_size
        chunk = text[start:end]
        chunks.append(chunk)

    return chunks


def split_pages(
        pages: list[dict],
        chunk_size: int = 500,
        chunk_overlap: int = 80,
) -> list[dict]:
    chunks = []

    for page in pages:
        page_chunks = split_text(
            page["text"],
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
        )

        for chunk_index,chunk_text in enumerate(page_chunks):
            chunk_data = {
                "text": chunk_text,
                "source": page["source"],
                "page": page["page"],
                "chunk_id": chunk_index,
            }

            chunks.append(chunk_data)

    return chunks

