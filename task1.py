from translate import Translator

def translate_to_german(word):
    translator = Translator(to_lang="de")
    translation = translator.translate(word)
    return translation

def main():
    word_to_translate = input("Enter the word to translate to German: ")
    translated_word = translate_to_german(word_to_translate)
    print(f"Translation: {translated_word}")

if __name__ == "__main__":
    main()
