# -*- coding: utf-8 -*-

"""
Simple Factory pattern

The most major problem of Simple Factory pattern is,
work mission is too heavy for Factory, every new Product
added need to modify your code.

"""


class AbstractDecoder(object):
    """
    Abstract Product
    """
    pass


class UTF8Decoder(AbstractDecoder):
    """
    Concrete Product
    """

    @staticmethod
    def decode(message):
        return repr(message.decode('utf-8'))


class GBKDecoder(AbstractDecoder):
    """
    Concrete Product
    """

    @staticmethod
    def decode(message):
        return repr(message.decode('gbk'))


class DecoderFactory(object):
    """
    Simple Factory
    """

    def __init__(self, encoding='utf-8'):
        self.encoding = encoding

    def decode(self, message):
        encodings = {"utf-8": UTF8Decoder, "gbk": GBKDecoder}
        return encodings[self.encoding]().decode(message)


if __name__ == '__main__':
    utf8_decoder = DecoderFactory("utf-8")
    print utf8_decoder.decode("简单工厂")

    gbk_decoder = DecoderFactory("gbk")
    print gbk_decoder.decode("简单工厂".decode("utf-8").encode("gbk"))