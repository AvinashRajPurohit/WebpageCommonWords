import html2text
from re import sub as re_sub
from itertools import chain
from collections import Counter
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk import download as nltk_download
from core.exceptions.common import CleanHtmlException
nltk_download('punkt')


def remove_spacial_chars(text: str) -> str:
    """function will remove spacial chars
    :param text: text with spacial chars
    :return: text without spacial chars
    """
    return re_sub(r'[^A-Za-z0-9]+', ' ', text)


def clean_html(data: str) -> str:
    """helper function for cleaning the html content
    :param: data = Html data that we want to clean
    :return: plain text from html
    """
    try:
        handler: html2text.HTML2Text = html2text.HTML2Text()
        handler.ignore_links = handler.ignore_images \
            = handler.ignore_tables = handler.ignore_emphasis = True

        data = handler.handle(data)
        return remove_spacial_chars(data)
    except Exception as e:
        print(e)
        raise CleanHtmlException("Something went wrong while cleaning html...")


def count_words_occurrences(cleaned_text: str) -> dict:
    """
    :param cleaned_text: cleaned html text
    :return: words and their occurrences
    """
    wordlist: list = list(chain(*[word_tokenize(s) for s in sent_tokenize(cleaned_text)]))
    counter_word_list: Counter = Counter(wordlist)

    data: dict = dict(counter_word_list)
    sorted_data: dict = dict(sorted(data.items(), key=lambda item: item[1], reverse=True))
    return sorted_data
