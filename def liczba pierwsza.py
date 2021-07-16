# wyznaczanie liczb pierwszych
def czy_pierwsza(liczba):
    if liczba == 2:
        return True
    if liczba % 2 == 0 or liczba <= 1:
        return False

    pierw = int(liczba ** 0.5) + 1
    for dzielnik in range(3, pierw, 2):
        if liczba % dzielnik == 0:
            return False
    return True
# zakres z którego są wyznaczane liczby pierwszw
for i in range(1, 20):
	if czy_pierwsza(i + 1):
			print(i + 1, end=" ")
print()