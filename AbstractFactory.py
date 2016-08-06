# -*- coding: utf-8 -*-

"""
Abstract Factory pattern

In Factory Method pattern, one Factory produce one product
which in one kind of products, but Abstract Factory mapping
 to many products in different kinds of product family.

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


class AbstractEncoder(object):
    """
    Abstract Encoder
    """
    pass


class UTF8Encoder(AbstractEncoder):
    """
    Concrete Product
    """

    @staticmethod
    def encode(message):
        return repr(message.encode('utf-8'))


class GBKEncoder(AbstractEncoder):
    """
    Concrete Product
    """

    @staticmethod
    def encode(message):
        return repr(message.encode('gbk'))


class AbstractFactory(object):
    """
    Abstract Factory
    """
    def __init__(self, codes, encoding):
        self.codes = codes
        self.encoding = encoding

        self.codec = {"encoder": EncoderFactory, "decoder": DecoderFactory}

    def decode(self, message):
        return self.codec[self.codes](encoding=self.encoding).decode(message)

    def encode(self, message):
        return self.codec[self.codes](encoding=self.encoding).encode(message)


class DecoderFactory(AbstractFactory):
    """
    Concrete Factory
    """

    def __init__(self, encoding='utf-8'):
        self.encoding = encoding

    def decode(self, message):
        encodings = {"utf-8": UTF8Decoder, "gbk": GBKDecoder}
        return encodings[self.encoding]().decode(message)


class EncoderFactory(AbstractFactory):
    """
    Concrete Factory
    """

    def __init__(self, encoding='utf-8'):
        self.encoding = encoding

    def encode(self, message):
        encodings = {"utf-8": UTF8Encoder, "gbk": GBKEncoder}
        return encodings[self.encoding]().encode(message)


if __name__ == '__main__':
    utf8_encoder = AbstractFactory("encoder", "utf-8")
    print utf8_encoder.encode(u"工厂方法")
    utf8_decoder = AbstractFactory("decoder", "utf-8")
    print utf8_decoder.decode("工厂方法")

    gbk_encoder = AbstractFactory("encoder", "gbk")
    print gbk_encoder.encode(u"工厂方法")
    gbk_decoder = AbstractFactory("decoder", "gbk")
    print gbk_decoder.decode("工厂方法".decode("utf-8").encode("gbk"))