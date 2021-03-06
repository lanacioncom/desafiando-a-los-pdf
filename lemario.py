#!/usr/bin/env python
# -*- coding: utf-8 -*-
import bisect

class Lemario:
    def __init__(self):
        self.spelling_file = 'data/spelling.txt'
        self.lemario_file = 'data/lemario.txt'
        self.error_file = 'data/error.txt'
        self.lemario_list = []
        self.spelling_wrong_list = []
        self.spelling_right_list = []
        self._generate_lists()

    def check_word(self, word):
        #word = self._check_spelling(word.lower())
        #try:
        #    return self.lemario_list.index(word) > -1
        #except:
        #    return False
        tWord = word.lower()
        i = bisect.bisect_left(self.lemario_list, tWord)
        if i != len(self.lemario_list) and self.lemario_list[i] == word:
            return True

        return False

    def _check_spelling(self, word):
        try:
            i = self.spelling_wrong_list.index(word)
            return self.spelling_right_list[i]
        except:
            return word

    def _generate_lists(self):
        with open(self.spelling_file, 'r') as spelling:
            for words in spelling:
                wrong, right = words.strip().split('->')
                self.spelling_wrong_list.append(wrong)
                self.spelling_right_list.append(right)

        with open(self.lemario_file, 'r') as lemario:
            for w in lemario:
                self.lemario_list.append(w.strip())

if __name__ == "__main__":
    lemario = Lemario()
    print lemario.check_word("abaxxx")
    print lemario.check_word("abaxxx1")
    print lemario.check_word("abaxxx2")
    print lemario.check_word("hola")
