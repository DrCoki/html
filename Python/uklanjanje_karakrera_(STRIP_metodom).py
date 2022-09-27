dan = input("Unesite dan:").lstrip("0")
mesec = input("Unesite mesec (broj):").lstrip("0")
godina = input("Unesite godinu")

datum = dan+"."+mesec+"."+godina+"."

print(datum)

#STRIP - uklanja karaktere sa pocetka i kraja texta (mira se oznaciti koji karakter zalis da uklonis)
#LSTRIP - uklanja karaktere sa leve strane
#RSTRIP - uklanja karaktere sa desne strane