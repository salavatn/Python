from ..converter.currancy import Converter

converter = Converter(from_currency='RUB')
print(converter.get_convert())