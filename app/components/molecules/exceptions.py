class TooLongStringError(Exception):
    def __str__(self):
        return '引数の文字列が長すぎます。'


class TooShortStringError(Exception):
    def __str__(self):
        return '引数の文字列が短すぎます。'
