from lib.polishNotation import PolishNotation
from config.config import config
from function.parse import parse

pn = PolishNotation(config, parse)
print(pn('7 22 2'))
print(pn('- 43 50'))
print(pn('* 5 4'))
print(pn('/ 70 0'))
