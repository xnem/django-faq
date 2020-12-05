from janome.tokenizer import Token
from nltk.stem.porter import PorterStemmer


STOPWORDS = ("is", "was", "to", "the")
ps = PorterStemmer()

def is_token_instance(token):
    return isinstance(token, Token)


class TokenFilter:
    @classmethod
    def filter(cls, token):
        raise NotImplementedError


class StopWordFilter(TokenFilter):
    @classmethod
    def filter(cls, token):
        if isinstance(token, Token):
            if token.surface in STOPWORDS:
                return None
        if token in STOPWORDS:
            return None
        return token


class Stemmer(TokenFilter):
    # 単語の語幹を取り出す処理 ex)dogs ⇒ dog
    @classmethod
    def filter(cls, token: str):
        if token:
            return ps.stem(token)


class POSFilter(TokenFilter):
    # 助詞/副詞/記号を除くフィルター
    @classmethod
    def filter(cls, token):
        stop_pos_list = ("助詞", "副詞", "記号")
        if any([token.part_of_speech.startswith(pos) for pos in stop_pos_list]):
            return None
        return token