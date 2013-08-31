#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Lemario:
    def __init__(self):
        self.lemario = open('data/lemario.txt', 'r')
        self.spelling = open('data/spelling.txt', 'r')
        self.lemario_list = []
        self.spelling_wrong_list = []
        self.spelling_right_list = []
        self._generate_lists()

    def check_word(self, word):
        word = self._check_spelling(word.lower())
        try:
            return self.lemario_list.index(word) > -1
        except:
            return False


    def _check_spelling(self, word):
        try:
            i = self.spelling_wrong_list.index(word)
            return self.spelling_right_list[i]
        except:
            return word

    def _generate_lists(self):
        for words in self.spelling:
            wrong, right = words.strip().split('->')
            self.spelling_wrong_list.append(wrong)
            self.spelling_right_list.append(right)

        for w in self.lemario:
            self.lemario_list.append(w.strip())

if __name__ == "__main__":
    lemario = Lemario()
    print lemario.check_word("abaxxx")
