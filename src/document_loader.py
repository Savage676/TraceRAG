import pymupdf
def count_pdf_pages(pdf_bytes: bytes) -> int:
    document = pymupdf.open(
        stream=pdf_bytes,
        filetype="pdf",
    )

    page_count = len(document)
    document.close()
    return page_count

def extract_pdf_pages(pdf_bytes: bytes,file_name: str) -> list[dict]:
    document = pymupdf.open(
        stream=pdf_bytes,
        filetype="pdf",
    )

    pages = []
    for page_index,page in enumerate(document):
        text = page.get_text("text").strip()

        if not text:
            continue

        page_data = {
            "text": text,
            "source": file_name,
            "page": page_index + 1,
        }

        pages.append(page_data)

    document.close()

    return pages
