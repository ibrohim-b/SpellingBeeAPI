from typing import Optional

from dictionary_sdk import ExtraInfo


class Word:
    def __init__(self, word_id: str, word: str, word_translation: str, extra_info: Optional[ExtraInfo]):
        self.word_id = word_id
        self.word_spell = word
        self.word_translation = word_translation
        self.extra_info = extra_info

    def __str__(self):
        return f"Word(word_id = {self.word_id}, word = {self.word_spell}, word_translation = {self.word_translation})"
