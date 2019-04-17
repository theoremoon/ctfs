from Crypto.Util.number import bytes_to_long
from binascii import unhexlify, hexlify
from ptrlib import *


n = 143683020644322299318564543310032550731362229816998143115532955396082143235946288551633953435584612777128870426064762700722474983419557070478193865039092489162972540442193198467681495674219822666567094248226655965731005254314292588896865658797569039580229607586511231175110747375426393447205505697507722501469
e = 3


c = 0x4bbd08e630c706c6d9e5757d3392f4aef603ed7e34f649666b8796afe772bcee84ca6882fec351dac1003861fc3a8f306a232d381f36714f41119f8df37fab0e07e02965898913bc349ca4aa4a275498ab85444664480d3ff72b707844d57a1b40658529d375ada1df10a1f867527f2686ea27392af83cdbf8f4bd9ebc46604a

for password in brute_force_attack(3):
    x = brute_force_pattern(password)
    m = "FLAG_300{{{}0513a1db877145db49b38f80f8fe7a6c6c9912b67d6a9a6d2c8dada7e15e}}".format(x)
    m2 = int(hexlify(m.encode()), 16)

    if pow(m2, e, n) == c:
        print(m)
        exit()
