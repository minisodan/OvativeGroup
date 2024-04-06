import cohere

__co = cohere.Client(
    api_key="52mmmG91mKfuEXARLx4KRzKq448QqGdUiQgDhZNd",
)


def coherence() -> str:
    """
    Returns a coherent output combining the given data.
    :return:
    """
    chat = __co.chat(
        message=f"make a coherent sentence out of list of text {['#WANNASIP?', 'ad', 'SPRITE', 'man with beard sitting next to 6', 'adele', 'purple soda', 'coca cola', 'charlie brown', 'iphone 15', 'iphone14', 'iphone13', 'iphone12']}! Only give the caption without creating an image.",
        model="command"
    )

    return chat.text


if __name__ == "__main__":
    print(coherence())
