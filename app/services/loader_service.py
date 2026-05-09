from trafilatura import fetch_url, extract, extract_metadata
from langsmith import traceable


@traceable(name="load_article")
def load_article(url: str):

    try:
        downloaded = fetch_url(url)

        if not downloaded:
            raise Exception("Failed to download article")

        metadata = extract_metadata(downloaded)

        content = extract(
            downloaded,
            include_comments=False,
            include_tables=False,
            include_links=False,
            include_images=False,
            favor_precision=True,
            deduplicate=True
        )

        if not content:
            raise Exception("Failed to extract article content")

        return {
            "title": metadata.title if metadata else "News Article",
            "content": content,
            "source_url": url,
        }

    except Exception as e:
        raise Exception(
            f"Failed to process URL: {url} | Error: {str(e)}"
        )