import re


# 共通のインターフェース
class CharacterFilterInterface:
    @classmethod
    def filter(cls, text: str):
        raise NotImplementedError


# 正規表現でhtmlタグを除去
class HtmlStripFilter(CharacterFilterInterface):
    @classmethod
    def filter(cls, text: str):
        html_pattern = re.compile(r"<[^>]*?>")
        return html_pattern.sub("", text)


# アルファベットをlowercaseに変換
class LowercaseFilter(CharacterFilterInterface):
    @classmethod
    def filter(cls, text: str):
        return text.lower()