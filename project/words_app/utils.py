import re
import string


def remove_numbers(text):
    return  re.sub(r'[0-9]+', '', text)

def remove_punctuation(text):
    return text.translate(str.maketrans('', '', string.punctuation))

def count_words(text):
    cleaned_text = remove_numbers(text)
    cleaned_text = remove_punctuation(cleaned_text)
    return len(cleaned_text.split())
