import cohere

__co = cohere.Client(
    api_key="52mmmG91mKfuEXARLx4KRzKq448QqGdUiQgDhZNd",
)


def coherence(con_caption: str, unc_caption: str, ocr_output: list[str]) -> str:
    """
    Returns a coherent output combining the given data.
    :return:
    """
    chat = __co.chat(
        message=f"You are tasked with processing inputs from two models: an Image Captioning model and an OCR ("
                f"Optical Character Recognition) model, which have analyzed an advertisement image. Your goal is to "
                f"synthesize their outputs into one coherent sentence that accurately describes the image. Please "
                f"adhere to the following guidelines to ensure the quality and relevance of your output. "
                f"Generalize Brand References: If the inputs do not specify a brand, avoid using "
                f"specific brand names in your "
                f"description. For example, if the input pertains to a beer but does not mention a specific brand, "
                f"refer to it as a 'beverage' or similar general term do not make any suggestions of what it might be."
                f" Second Guideline Maintain Grammatical Integrity: Do not include "
                f"any words in the final sentence that are grammatically incorrect. Ensure that the output is "
                f"linguistically sound and follows standard grammar rules. Do Not Add Context When Context Is Not Give:"
                f" an example of this might be speculating on the context around the image or adding elements "
                f"when you are not given them."
                f"If you are given any brands in the Optical Character Recognition output please use them: "
                f"for example if you are given Colgate or Sprite, mention them in the output caption."
                f"Third Guideline Start Every Caption With: 'The Advertisement seems to be '"
                f"If You are Given a Celebrity Name Use It: Do NOT describe them and do not give extra "
                f"context on the celebrity. Only say that they are in the Ad"
                f"Final Guideline: ONLY respond with the caption you have generated and NOTHING more. DO NOT ask me how "
                f"you can be more helpful I ONLY want you to provide the caption you will be generating."
                f"these are captions of an image generated from the salesforce blip model: {con_caption},"
                f"{unc_caption} and easyocr read the following words from the image: {ocr_output}, ",
        model="command"
    )

    return chat.text

if __name__ == "__main__":
    print(coherence())
