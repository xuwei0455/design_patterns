# -*- coding: utf-8 -*-

"""
Factory Method pattern

The distinction of Simple Factory and Factory Method is,
Simple Factory pattern only offer one factory to produce,
otherwise, Factory Method can horizontal scaling by add
new Factory.

And, when there just one factory, pattern fall back to
Simple Factory.

When just one concrete product is perhaps returned,
factory patterns will lose the existence, you can just
create the object directly.
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
    pass


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
    utf8_encoder = EncoderFactory("utf-8")
    print utf8_encoder.encode(u"工厂方法")
    utf8_decoder = DecoderFactory("utf-8")
    print utf8_decoder.decode("工厂方法")

    gbk_encoder = EncoderFactory("gbk")
    print gbk_encoder.encode(u"工厂方法")
    gbk_decoder = DecoderFactory("gbk")
    print gbk_decoder.decode("工厂方法".decode("utf-8").encode("gbk"))