from . import CharacterFilter
from . import Tokenizer
from . import TokenFilter

class Analyzer:   

    char_filters = [CharacterFilter.HtmlStripFilter(), CharacterFilter.LowercaseFilter()]
    tokenizers = [Tokenizer.JanomeTokenizer()]
    token_filters = [TokenFilter.StopWordFilter(), TokenFilter.Stemmer(), TokenFilter.POSFilter()]


    @classmethod
    def analyze(cls, text: str):
        text = cls._char_filter(text)
        tokens = cls._tokenizer(text)
        filtered_tokens = {}
        for token in tokens:
            print(token)
            filtered_token = cls._token_filter(token)
            if not(filtered_token is None): # フィルターにかかった不要なtokenがNone
                # 出現回数をカウント
                if filtered_token.surface in filtered_tokens.keys():
                    filtered_tokens[filtered_token.surface] += 1
                else:
                    filtered_tokens[filtered_token.surface] = 1
        return filtered_tokens

    @classmethod
    def _char_filter(cls, text):
        # CharFilterクラスぶん回してフィルターにかけていく(CharacterFilter.py)
        for char_filter in cls.char_filters:
            text = char_filter.filter(text)
        return text

    @classmethod
    def _tokenizer(cls, text):
        # Tokenizerクラス文回してtextを好ましい形でtoken化する(Tokenizer.py)
        for tokenizer in cls.tokenizers:
            tokens = tokenizer.tokenize(text)
            return tokens

    @classmethod
    def _token_filter(cls, token):
        # TokenFilterクラスぶん回してフィルターにかけていく(TokenFilter.py)
        for token_filter in cls.token_filters:
            try:
                token = token_filter.filter(token)
            except:
                continue
        return token
