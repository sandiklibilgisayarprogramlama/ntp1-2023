"""
x^2+5x-y
problemini fonksiyon ve modül kullanarak çözelim.
"""

from sys import builtin_module_names
from islem import *

x = 10
y = 20
print(x**2+5*x-y)
x2 = kare_al(x)
toplam_sonuc = topla(x2, carp(5, x))
sonuc = cikar(toplam_sonuc, y)
print(sonuc)
