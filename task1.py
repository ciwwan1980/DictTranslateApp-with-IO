
from translate import Translator
import json
import io

def load_dictionary():
    try:
        with open('dictionary.json', 'r') as file:
            dictionary = json.load(file)
        return dictionary
    except FileNotFoundError:
        return {}
    

def save_dictionary(dictionary):
    with open('dictionary.json', 'w') as file:
        json.dump(dictionary, file, indent=2)


def translate_word(word, dictionary):
    if word in dictionary:
        translation = dictionary[word]
        print(f"Translation: {translation}")
    else:
        translator = Translator(to_lang="de")
        translation = translator.translate(word)
        print(f"Translation: {translation}")
        return translation
    
def remove_translation(word, dictionary):
    if word in dictionary:
        del dictionary[word]
        print(f"Translation for {word} removed successfully.")
        save_dictionary(dictionary)
    else:
        print(f"Word {word} not found in the dictionary.")


def update_translation(word, dictionary):
    if word in dictionary:
        old_translation = dictionary[word]
        new_translation = input(f"Enter the new translation for '{word}' (current translation: {old_translation}): ")
        dictionary[word] = new_translation
        save_dictionary(dictionary)
        print(f"Translation updated successfully: {word} -> {new_translation}")
    else:
        print(f"Word '{word}' not found in the dictionary.")


def main():
    dictionary = load_dictionary()     

    while True: 
        print("1.Translate word")
        print("2. Add translation")
        print("3.List of all translation")
        print("4. remove translation")
        print("5. Update translation")
        print("6. Exit")


        choice=input("Enter your choices (1/2/3/4/5): ")

        if choice == '1':

            word_to_translate = input("Enter the word to translate: ")
            translate_word(word_to_translate, dictionary)

        elif choice == '2':

            new_word = input("Enter the new word: ")
            translation = translate_word(new_word, dictionary)

            if new_word not in dictionary:
                dictionary[new_word] = translation
                save_dictionary(dictionary)
                print(f"Translation added: {new_word} -> {translation}")

        elif choice == '3':
             
            print("List all translations in dictionary:")
            if not dictionary:
                print("Dictionary is empty.")
            else:
                for word, translation in dictionary.items():
                    print(f"{word} -> {translation}")
        elif choice == '4':
            word_to_remove = input("Enter the word to remove: ")
            remove_translation(word_to_remove, dictionary)

        elif choice == '5':
            word_to_update = input("Enter the word to update: ")
            update_translation(word_to_update, dictionary)

        elif choice == '6':
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please enter 1, 2, 3, 4, 5, or 6.")

if __name__ == "__main__":
    main()