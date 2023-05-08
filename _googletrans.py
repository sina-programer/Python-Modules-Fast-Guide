from googletrans import Translator  # pip install googletrans

translator = Translator()
translation = translator.translate("سلام به همه")
print(f"{translation.origin} ({translation.src}) --> {translation.text} ({translation.dest})")

# translator.detect(text)  # determines the language
