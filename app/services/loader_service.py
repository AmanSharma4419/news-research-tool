from newspaper import Article


def load_article(url: str):

    try:

        article = Article(url)

        article.download()
        article.parse()

        if not article.text:
            raise Exception("Empty article text")

        return {
            "title": article.title,
            "text": article.text,
            "source_url": url
        }

    except Exception as e:

        raise Exception(
            f"Failed to process URL: {url} | Error: {str(e)}"
        )