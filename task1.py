from translate import Translator
import json

def load_dictionary():
    try:
        with open('dictionary.json', 'r') as file:
            dictionary = json.load(file)
        return dictionary
    except FileNotFoundError:
        return {}

def main():
    dictionary = {} 

    while True: 
        print("1.Translate word")
        print("2. Add translation")
        print("3.List of all translation")
        print("4. remove translation")
        print("4. Exit")


        choice=input("Enter your choices (1/2/3/4/5) ")

        if choice == '1':

            word_to_translate = input("Enter the word to translate: ")
            
            translation = dictionary.get(word_to_translate, None)

            if translation is None:
                translator = Translator(to_lang="de")
                translation = translator.translate(word_to_translate)
                print(f"Translation: {translation}")
            else:
                print(f"Translation: {translation}")

        elif choice == '2':
             pass
        elif choice == '3':
             pass
        elif choice == '4':
             pass
        elif choice == '5':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, 4, or 5.")

if __name__ == "__main__":
    main()