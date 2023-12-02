
from translate import Translator
import json

# def load_dictionary():
#     try:
#         with open('dictionary.json', 'r') as file:
#             dictionary = json.load(file)
#         return dictionary
#     except FileNotFoundError:
#         return {}
    

def save_dictionary(dictionary):
    with open('dictionary.json', 'w') as file:
        json.dump(dictionary, file, indent=2)

def main():
    dictionary = {}     

    while True: 
        print("1.Translate word")
        print("2. Add translation")
        print("3.List of all translation")
        print("4. remove translation")
        print("4. Exit")


        choice=input("Enter your choices (1/2/3/4/5): ")

        if choice == '1':

            word_to_translate = input("Enter the word to translate: ")
            
            # translation = dictionary.get(word_to_translate, None)

            if word_to_translate in dictionary:
                translation=dictionary[word_to_translate]
                print(f"Translation: {translation}")
            else:
                translator = Translator(to_lang="de")
                translation = translator.translate(word_to_translate)
                print(f"Translation: {translation}")

        elif choice == '2':
            new_word = input("Enter the new word: ")

            if new_word in dictionary:
                print(f"{new_word} already exists in the dictionary. The existing translation is: {dictionary[new_word]}")
            else:
                translator = Translator(to_lang="de")
                new_translation = translator.translate(new_word)

                dictionary[new_word] = new_translation
                save_dictionary(dictionary)

                print(f"Translation added: {new_word} -> {new_translation}")

        elif choice == '3':
             
            print("List all translations in dictionary:")
            if not dictionary:
                print("Dictionary is empty.")
            else:
                for word, translation in dictionary.items():
                    print(f"{word} -> {translation}")
        elif choice == '4':
             pass
        elif choice == '5':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, 4, or 5.")

if __name__ == "__main__":
    main()