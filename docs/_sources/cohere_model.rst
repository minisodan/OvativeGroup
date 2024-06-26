Coherence Model
===============

Coherence Function
------------------

.. function:: coherence(con_caption: str, unc_caption: str, ocr_output: list[str]) -> str

    Generates a coherent output by combining data from an image captioning model and an Optical Character Recognition (OCR) model.

    :param con_caption: The conditional image caption generated by the image captioning model.
    :type con_caption: str
    :param unc_caption: The unconditional image caption generated by the image captioning model.
    :type unc_caption: str
    :param ocr_output: The output text generated by the Optical Character Recognition (OCR) model.
    :type ocr_output: list[str]
    :return: A coherent sentence describing the image, adhering to specific guidelines.

    Synthesizes outputs from an image captioning model and an OCR model into one coherent sentence describing the image. It follows specific guidelines to ensure the quality, relevance, and grammatical integrity of the output.

Guidelines:
-----------

    1. **Generalize Brand References:** If brand names are not specified in the inputs, avoid using specific brand names in the description.
    2. **Maintain Grammatical Integrity:** Ensure that the output follows standard grammar rules and does not include any grammatically incorrect words.
    3. **Do Not Add Context When Context Is Not Given:** Avoid speculating on the context around the image or adding elements that are not provided.
    4. **Utilize OCR Brand Names:** If brand names are detected in the OCR output, incorporate them into the output caption.
    5. **Start Every Caption With:** "The advertisement seems to be ".
    6. **Utilize Celebrity Names:** If celebrity names are provided, mention them in the output without providing additional context.
    7. **Final Guideline:** Output only the final caption without additional information.

Example usage:
--------------

    .. code-block:: python

        from coherence_module import coherence

        con_caption = "A photo of a scenic beach"
        unc_caption = "An image showing a beautiful sunset"
        ocr_output = ["Colgate", "Sprite"]

        output_caption = coherence(con_caption, unc_caption, ocr_output)
        print("Output Caption:", output_caption)

