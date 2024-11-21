# Uzraksti programmu, kurā  dators izvēlas 100 skaitļus robežās no 101 līdz 500. Izvēlētie skaitļi tiek izvadīti terminālī.

import random

for i in range(101, 501, 1):
    skaitlis=random.randint(101,501,5)
    print(skaitlis)
