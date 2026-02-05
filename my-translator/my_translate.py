from translate import Translator


translator = Translator(to_lang="ja")


try:
    with open("./english.txt", "r") as english_file:
        text = english_file.read()
        translation = translator.translate(text)  # fixed spelling

        with open("./japanese.txt", "w") as japanese_file:
            japanese_file.write(translation)

    # reopen to read the output
    with open("./japanese.txt", "r") as japanese_file:
        print(japanese_file.read())

except Exception as e:
    print("Error:", e)
