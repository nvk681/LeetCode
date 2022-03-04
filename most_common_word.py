import string
punc = string.punctuation

class Solution:
    def mostCommonWord(self, paragraph: str, banned) -> str:
        normalized_str = ''.join([c.lower() if c.isalnum() else ' ' for c in paragraph])
        paragraph = normalized_str.split()
        filter_words = list(set(paragraph) - set(banned))
        word_max = ""
        max_count = 0
        for word in filter_words:
            current_count = paragraph.count(word)
            if current_count > max_count:
                max_count = current_count
                word_max = word

        return word_max