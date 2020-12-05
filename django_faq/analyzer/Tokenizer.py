from janome.tokenizer import Tokenizer
import re

tokenizer = Tokenizer()

class BaseTokenizer:
    @classmethod
    def tokenize(cls, text):
        raise NotImplementedError


class JanomeTokenizer(BaseTokenizer):
    @classmethod
    def tokenize(cls, text):
        return ( t for t in tokenizer.tokenize(text))