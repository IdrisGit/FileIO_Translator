from translate import Translator

translator = Translator(to_lang="ja")

try:
    with open("./test.txt", mode="r") as my_file:
        # print(my_file.read())
        test_en = my_file.read()
        translation_ja = translator.translate(test_en)
        print(translation_ja)
        test_ja = translation_ja

        with open("./test-ja.txt", mode="w") as my_file_ja:
            my_file_ja.write(test_ja)
            #print(test_ja)
except FileNotFoundError:
    print("File Error")
