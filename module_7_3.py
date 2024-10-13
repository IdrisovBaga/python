import os
import string


class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = list(file_names)
        self._ensure_files_exist()

    def _ensure_files_exist(self):
        for file_name in self.file_names:
            if not os.path.exists(file_name):
                with open(file_name, 'w', encoding='utf-8') as file:
                    pass

    def _clean_word(self, word):
        return word.strip(string.punctuation).lower()

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as file:
                words = [self._clean_word(word) for word in file.read().split()]
                all_words[file_name] = words
        return all_words

    def find(self, search_word):
        word_positions = {}
        for file_name, words in self.get_all_words().items():
            positions = [index + 1 for index, word in enumerate(words) if word.lower() == search_word.lower()]
            if positions:
                word_positions[file_name] = positions
        return word_positions

    def count(self, search_word):
        word_count = {}
        for file_name, words in self.get_all_words().items():
            count = sum(1 for word in words if word.lower() == search_word.lower())
            word_count[file_name] = count
        return word_count


finder2 = WordsFinder('test_file.txt')

print(finder2.get_all_words())
print(finder2.find('TEXT'))
print(finder2.count('teXT'))