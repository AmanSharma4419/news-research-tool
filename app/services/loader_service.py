from trafilatura import fetch_url, extract


def load_article(url: str):

    try:

        downloaded = fetch_url(url)

        if not downloaded:
            raise Exception("Failed to download article")

        content = extract(
            downloaded,
            include_comments=False,
            include_tables=False
        )

        if not content:
            raise Exception("Failed to extract article content")

    

        return {
            "title": "News Article",
            "content": content,
            "source_url": url
        }
    except Exception as e:

        raise Exception(
            f"Failed to process URL: {url} | Error: {str(e)}"
        )