from analyzer import word_count, unique_word_count, most_common_word


def run():
    text = input("Enter text: ")

    print(f"Total words: {word_count(text)}")
    print(f"Unique words: {unique_word_count(text)}")

    common = most_common_word(text)
    if common:
        print(f"Most common word: '{common[0]}' ({common[1]} times)")
    else:
        print("No words found.")


if __name__ == "__main__":
    run()
