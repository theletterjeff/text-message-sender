"""Load texts from file. Acceptable file formats
include .csv and .txt. There should be one text
per line in the file."""

import csv
import itertools
import os

class LoadTexts:
    """Load texts from file"""

    def __init__(self, texts_filepath):
        self.texts_filepath = texts_filepath

        # Map file extension to function
        self.extension = os.path.splitext(texts_filepath)[1]
        self.func_dict = {
            '.csv': self._load_csv,
            '.txt': self._load_txt,
        }

    @property
    def texts(self):
        """Property to load/access text messages"""
        return self.func_dict[self.extension]()

    def _load_csv(self, encoding='utf-8-sig'):
        """Load text content from .csv file"""
        with open(self.texts_filepath, 'r', encoding=encoding) as file:
            csv_reader = csv.reader(file)
            return list(itertools.chain(*csv_reader))

    def _load_txt(self):
        """Load text content from .txt file"""
        with open(self.texts_filepath, 'r', encoding='utf-8-sig') as file:
            text_list = file.readlines()
            return [text.replace('\n', '') for text in text_list]
