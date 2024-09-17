from address import Address
from mailing import Mailing

to_address = Address(126548, "Краснодар", "Комсомольская", 8, 103)
from_address = Address(158725, "Москва", "Ленинский проспект", 8, 65)

mailing = Mailing(to_address, from_address, 1000, 18452689623145)

print(mailing)
