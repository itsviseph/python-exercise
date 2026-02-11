from collections import Counter
import re


def normalize_text(text):
    """
    Lowercases text and removes non-alphanumeric characters.
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string")

    text = text.lower()
    text = re.sub(r"[^\w\s]", "", text)
    return text


def word_count(text):
    """
    Returns total number of words in the text.
    """
    text = normalize_text(text)

    if not text.strip():
        return 0

    words = text.split()
    return len(words)


def unique_word_count(text):
    """
    Returns number of unique words.
    """
    text = normalize_text(text)

    if not text.strip():
        return 0

    words = text.split()
    return len(set(words))


def most_common_word(text):
    """
    Returns the most common word and its count as a tuple.
    """
    text = normalize_text(text)

    if not text.strip():
        return None

    words = text.split()
    counter = Counter(words)

    word, count = counter.most_common(1)[0]
    return word, count
