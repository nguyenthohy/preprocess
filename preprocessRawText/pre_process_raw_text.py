# coding=utf-8
import csv

from django.http import JsonResponse
from flashtext import KeywordProcessor
from gensim.parsing.preprocessing import strip_non_alphanum, strip_numeric, split_alphanum, strip_short, \
    strip_multiple_whitespaces

from pyvi import ViTokenizer


class pre_process_raw_text:
    @staticmethod
    def clean_text(self, url_file=''):
        data_parse = {}
        keyword_processor = KeywordProcessor()
        keyword_processor.add_keyword_from_file('vietnamese-stopwords-dash.txt')

        with open('url_file', 'r+') as data_file:
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
                            contents_parsed = split_alphanum(contents_parsed)  # Xóa từ có số và chữ, vd a1 a2
                            contents_parsed = ViTokenizer.tokenize(contents_parsed)  # merge compound word

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
        return JsonResponse({'data': data_parse})

