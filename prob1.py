# Am o metoda ce primeste ca parametru 2 tablouri si returneaza un tablou nou cu elementele comune din cele doua tablouri
def tablouElementeComune(tablou1, tablou2):
    tablouComun = []
    for i in tablou1:
       for j in tablou2:
           if i == j:
               tablouComun.append(i)
    return tablouComun

tab1 = [12, 3, 4, 6, 0, 2]
tab2 = [4, 5, 3, 8, 12]

print(tablouElementeComune(tab1, tab2))

# Am o metoda ce primeste ca parametru un tablou de nr intregi si o valoare intreaga, caut toate perechile care au suma egala cu parametrul respectiv
val = 6
def perechiDeNumere(tablou, valoare):
    for i in tablou:
        for j in tablou:
            if (i+j == valoare) and (i!=j):
                print(f"Am gasit o pereche de numere care au suma egala cu {valoare}: {i} - {j}")

perechiDeNumere(tab1, val)

# Am o metoda care primeste un parametru si returneaza un nou tablou format din elementele cu valoare mai mare decat 100
tab3 = [102, 1, 3, 129, 30, 8, 1]
def nrMaiMari(tablou):
    tablouNou = []
    for i in tablou:
        if i > 100:
            tablouNou.append(i)

    return tablouNou

print("Numerele mai mari decat 100 sunt", nrMaiMari(tab3), sep=": ")

# Am o metoda ce primeste ca parametru un tablou de numere intregi si o variabila int, trebuie sa returnez un nou tablou care in loc de variabila 
# primita ca parametru are 0
# [110, 0, 2, 3, 4, 2] -> [110, 0, 0, 3, 4, 0]
valoareDeInlocuit = 1
def stergeValoare(tab, val):
    tablouNou = []
    for i in tab:
        if i == val:
            tablouNou.append(0)
        else:
            tablouNou.append(i)

    return tablouNou

print(f"Am inlocuit cu 0 cifrele de {valoareDeInlocuit}, iar rezultatul este: ", stergeValoare(tab3, valoareDeInlocuit))
