# coding=utf-8
import csv

import pkg_resources
from flashtext import KeywordProcessor
from gensim.parsing.preprocessing import strip_non_alphanum, strip_numeric, split_alphanum, strip_short, \
    strip_multiple_whitespaces

from pyvi import ViTokenizer
import json


def clean_text_file(url_file=''):
    data_parse = {}
    try:
        keyword_processor = KeywordProcessor()
        keyword_processor.add_keyword_from_file(pkg_resources.resource_filename(__name__,'vietnamese-stopwords-dash.txt'))

        with open(url_file, 'r+') as data_file:
            data = csv.reader(data_file)
            for row in data:
                i = 0
                for sentence in row:
                    if i == 0:
                        key = sentence
                        sentence_parse = []
                    else:
                        try:
                            contents_parsed = strip_non_alphanum(sentence).lower().strip()  # Xóa các ký tự đặc biệt
                            contents_parsed = strip_numeric(
                                contents_parsed)  # Xóa các ký tự đặc biệt không phải chữ hoặc số
                            contents_parsed = ViTokenizer.tokenize(contents_parsed)  # phân từ đơn từ ghép

                            extract_stopwords = keyword_processor.extract_keywords(contents_parsed)
                            for stopword in extract_stopwords:
                                contents_parsed = contents_parsed.replace(stopword, '')  # xóa stopword

                            contents_parsed = strip_multiple_whitespaces(
                                contents_parsed)  # Chuẩn hóa để mỗi từ cách nhau một khoảng trắng
                            sentence_parse.append(contents_parsed)

                        except Exception as e:
                            return str(e)
                    i += 1
                data_parse[key] = sentence_parse
        return json.dumps(data_parse)
    except Exception as e:
        return str(e)


def clean_text(sentence=''):
    keyword_processor = KeywordProcessor()
    keyword_processor.add_keyword_from_file(pkg_resources.resource_filename(__name__,'vietnamese-stopwords-dash.txt'))

    try:
        contents_parsed = strip_non_alphanum(sentence).lower().strip()  # Xóa các ký tự đặc biệt
        contents_parsed = strip_numeric(
            contents_parsed)  # Xóa các ký tự đặc biệt không phải chữ hoặc số
        contents_parsed = ViTokenizer.tokenize(contents_parsed)  # phân từ đơn từ ghép

        extract_stopwords = keyword_processor.extract_keywords(contents_parsed)
        for stopword in extract_stopwords:
            contents_parsed = contents_parsed.replace(stopword, '')  # xóa stopword

        contents_parsed = strip_multiple_whitespaces(
            contents_parsed)  # Chuẩn hóa để mỗi từ cách nhau một khoảng trắng

    except Exception as e:
        return str(e)
    return json.dumps(contents_parsed)
