"""
import islem  # modul dahil edildi.


print(islem.topla(12, 12))
print(islem.cikar(12, 12))
print(islem.carp(12, 12))
print(islem.bol(12, 12))
print(islem.ust_hesapla(10, 2))
print(islem.program_ismi)


import islem as i
# as -> alias
print(i.bol(12, 6))


from islem import ust_hesapla
from islem import topla

print(ust_hesapla(2, 6))
print(topla(2, 6))
"""

#from islem import *
# hepsini dahil et

from islem import *


print(topla(10, 2))
print(program_ismi)
