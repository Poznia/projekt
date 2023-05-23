from pojistenec import Pojistenec
pojistenec = Pojistenec('jmeno', 'prijmeni', 'vek', 'telcislo')

prikaz = 1
while prikaz <= 3:
    print("--------------------------\n   EVIDENCE POJISTENCU\n--------------------------")
    print()
    print("Vyberte si akci:")
    print("1 - Pridat noveho pojisteneho")
    print("2 - Vypsat vsechny pojistene")
    print("3 - Vyhledat pojisteneho")
    print("4 - Konec")
    prikaz = int(input())

    if prikaz == 1:
        pojistenec.jmeno = input("Zadejte jmeno pojisteneho:")
        pojistenec.prijmeni = input("Zadejte prijmeni:")
        pojistenec.vek = input("Zadejte vek:")
        pojistenec.telcislo = input("Zadejte telefonni cislo:")

        File_data = open(r"C:\Users\pozni\PycharmProjects\pythonProject7\lekce\file.txt", "a")
        File_data.write(pojistenec.jmeno)
        File_data.write("   ")
        File_data.write(pojistenec.prijmeni)
        File_data.write("   ")
        File_data.write(pojistenec.vek)
        File_data.write("   ")
        File_data.write(pojistenec.telcislo)
        File_data.write('\n')
        File_data.close()

        print("Data byla ulozena.")
        print()

    elif prikaz == 2:
        File_data = open(r"C:\Users\pozni\PycharmProjects\pythonProject7\lekce\file.txt", "r")
        for radek in File_data.readlines():
            print(radek.strip())
        File_data.close()
        print()

    elif prikaz == 3:
        pojistenec.jmeno = input("Zadejte jmeno pojisteneho:")
        pojistenec.prijmeni = input("Zadejte prijmeni:")
        print()
        print("Tuto cast zadani se mi nepodarilo splnit - nedokazal jsem vymyslet, jak filtrovat data v txt souboru")
        print()

print("Dekuji za pouziti evidence.")
