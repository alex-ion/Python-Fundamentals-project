# Ion Sorin-Alexandru
# Proiect final curs Python Fundamentals

lista_produse = []


class Catalog():
    # """de completat"""
    global lista_produse
    clasa = ""
    subclasa = ""

    def __init__(self, pret, consum, producator):
        """Creare obiect"""
        self.pret = pret
        self.consum = consum
        self.producator = producator.upper()
        self.cod_produs = len(lista_produse) + 1
        lista_produse.append(self)

    def afisare(self):
        """Afisare tuturor produselor"""
        if lista_produse:
            print "\n"
            print "--------------------------------------------------------"
            print "CATALOGUL PRODUSELOR CONTINE IN ACEST MOMENT:\n".center(56)
        else:
            print "\n"
            print "--------------------------------------------------------"
            print "CATALOGUL NU CONTINE PRODUSE IN ACEST MOMENT:\n".center(56)
        i = 1
        for e in lista_produse:
            print "Produsul cu numarul " + str(i) + " este din categoria " + str(e.clasa) + ", subcategoria " + str(
                e.subclasa) + " si are urmatoarele caracteristici:"
            afisare(e)
            i += 1

    def sortare_pret(self):
        """Sortarea produselor dupa pret"""
        lista_produse.sort(key=lambda lista_produse: int(lista_produse.pret))
        print "--------------------------------------------------------"
        print "PRODUSELE ORDONATE DUPA PRET SUNT:\n".center(56)
        i = 1
        for e in lista_produse:
            print "Produsul cu numarul " + str(i) + " este din categoria " + str(e.clasa) + ", subcategoria " + str(
                e.subclasa) + " si are urmatoarele caracteristici:"
            afisare(e)
            i += 1

    def sortare_consum(self):
        """Sortarea produselor dupa consum"""
        lista_produse.sort(key=lambda lista_produse: int(lista_produse.consum))
        print "--------------------------------------------------------"
        print "PRODUSELE ORDONATE DUPA CONSUM SUNT:\n".center(56)
        i = 1
        for e in lista_produse:
            print "Produsul cu numarul " + str(i) + " este din categoria " + str(e.clasa) + ", subcategoria " + str(
                e.subclasa) + " si are urmatoarele caracteristici:"
            afisare(e)
            i += 1

    def sortare_producator(self, producator):
        """Sortarea produselor dupa producator"""
        temp = 0
        for e in lista_produse:
            if e.producator == producator:
                temp = 1
        if temp == 0:
            print "Nu au fost gasite produse de la producatorul " + str(producator)
        i = 1
        for e in lista_produse:
            if e.producator == producator:
                print "Produsul cu numarul " + str(i) + " este din categoria " + str(e.clasa) + ", subcategoria " + str(
                    e.subclasa) + " si are urmatoarele caracteristici:"
                afisare(e)
                i += 1


class Electrocasnice_Mari(Catalog):
    def creare_electrocasnic_mare(self, adancime, latime, inaltime):
        """Adaugare argumente specifice electrocasnicelor mari"""
        self.adancime = adancime
        self.latime = latime
        self.inaltime = inaltime


class Electrocasnice_Mici(Catalog):
    def creare_electrocasnic_mic(self, lungime_cablu, baterie):
        """Adaugare argumente specifice electrocasnicelor mici"""
        self.lungime_cablu = lungime_cablu
        self.baterie = baterie


class Frigider(Electrocasnice_Mari):
    def creare_frigider(self, capacitate_congelator, capacitate_frigider):
        """Adaugare argumente specifice frigiderelor"""
        self.capacitate_congelator = capacitate_congelator
        self.capacitate_frigider = capacitate_frigider


class Aragaz(Electrocasnice_Mari):
    def creare_aragaz(self, nr_arzatoare):
        """Adaugare argumente specifice aragazurilor"""
        self.nr_arzatoare = nr_arzatoare


class Mixer(Electrocasnice_Mici):
    def creare_mixer(self, rotatii_min):
        """Adaugare argumente specifice mixerelor"""
        self.rotatii_min = rotatii_min


class Fier_calcat(Electrocasnice_Mici):
    def creare_fier_calcat(self, rezervor):
        """Adaugare argumente specifice fiarelor de calcat"""
        self.rezervor = rezervor


def afisare(e):
    print "Producator: \t\t" + str(e.producator)
    print "Pret: \t\t\t" + str(e.pret)
    print "Consum: \t\t" + str(e.consum)
    print "Cod produs: \t\t" + str(e.cod_produs)
    try:
        e.adancime
    except:
        pass
    else:
        print "Adancime: \t\t" + str(e.adancime)

    try:
        e.latime
    except:
        pass
    else:
        print "Latime: \t\t" + str(e.latime)

    try:
        e.inaltime
    except:
        pass
    else:
        print "Inaltime: \t\t" + str(e.inaltime)

    try:
        e.lungime_cablu
    except:
        pass
    else:
        print "Lungime cablu: \t\t" + str(e.lungime_cablu)

    try:
        e.baterie
    except:
        pass
    else:
        print "Baterie: \t\t" + str(e.baterie)

    try:
        e.capacitate_congelator
    except:
        pass
    else:
        print "Capacitate congelator: \t" + str(e.capacitate_congelator)

    try:
        e.capacitate_frigider
    except:
        pass
    else:
        print "Capacitate frigider: \t" + str(e.capacitate_frigider)

    try:
        e.nr_arzatoare
    except:
        pass
    else:
        print "Numar arzatoare: \t" + str(e.nr_arzatoare)

    try:
        e.rotatii_min
    except:
        pass
    else:
        print "Rotatii pe minut: \t" + str(e.rotatii_min)

    try:
        e.rezervor
    except:
        pass
    else:
        print "Rezervor: \t\t" + str(e.rezervor)
    print "\n"


def introducere_produs():
    """Prima parte din procedura de introducere a unui produs"""
    while True:
        print "--------------------------------------------------------"
        print "MENIUL CURENT ESTE:".center(56)
        print """
1 - Introducere electrocasnic mare
2 - Introducere electrocasnic mic
Q - Pentru intoarcere la meniul anterior\n"""
        pickone = raw_input("Alege o optiune din meniu:\t")
        if pickone == "1":  # Introducere electrocasnic mare
            introducere_produs1("1")
        elif pickone == "2":  # Introducere electrocasnic mic
            introducere_produs1("2")
        elif pickone.upper() == "Q":  # Pentru intoarcere la meniul anterior
            break
        else:
            print "--------------------------------------------------------\n"
            print "OPTIUNEA INTRODUSA NU ESTE VALIDA.\n".center(56)


def verificare_digit(y, z):
    """Verifica daca atributul care trebuie introdus contine cifre"""
    while True:
        x = raw_input(y)
        if x.isdigit():
            return x
        else:
            print z + " nu poate contine alte caractere decat cifre."


def verificare_alpha(y, z):
    """Verifica daca atributul care trebuie introdus contine litere sau spatii"""
    while True:
        x = raw_input(y)
        temp = 0
        for e in x:
            if not (e.isalpha() or e == " "):
                temp = 1
        if temp == 0:
            return x
        else:
            print z + " nu poate contine alte caractere decat litere."


def introducere_produs1(var):
    """A doua parte din procedura de introducere a unui produs"""
    if var == "1":
        while True:
            print "--------------------------------------------------------"
            print "MENIUL CURENT ESTE:".center(56)
            print """
1 - Introducere frigider
2 - Introducere aragaz
Q - Pentru intoarcere la meniul anterior\n"""
            pickone = raw_input("Alege o optiune din meniu:\t")
            print "--------------------------------------------------------"
            if pickone == "1":  # Pentru introducere frigider
                print "INTRODUCERE FRIGIDER\n".center(56)
                a = verificare_alpha("Introduceti producatorul frigiderului:\t", "Numele producatorului")
                b = verificare_digit("Introduceti pretul frigiderului:\t", "Pretul")
                c = verificare_digit("Introduceti consumul frigiderului:\t", "Consumul")
                e = verificare_digit("Introduceti adancimea produsului:\t", "Adancimea")
                f = verificare_digit("Introduceti latimea produsului:\t\t", "Latimea")
                g = verificare_digit("Introduceti inaltimea produsului:\t", "Inaltimea")
                h = verificare_digit("Introduceti capacitatea congelatorului:\t", "Capacitatea congelatorului")
                i = verificare_digit("Introduceti capacitatea frigiderului:\t", "Capacitatea frigiderului")
                j = len(globals())
                globals()[j] = Frigider(b, c, a)
                globals()[j].creare_electrocasnic_mare(e, f, g)
                globals()[j].creare_frigider(h, i)
                globals()[j].clasa = "electrocasnice mari"
                globals()[j].subclasa = "frigider"
                print "\nProdusul a fost introdus in inventar cu codul: " + str(len(lista_produse))
            elif pickone == "2":  # Pentru introducere aragaz
                print "INTRODUCERE ARAGAZ\n".center(56)
                a = verificare_alpha("Introduceti producatorul aragazului:\t\t", "Numele producatorului")
                b = verificare_digit("Introduceti pretul aragazului:\t\t\t", "Pretul")
                c = verificare_digit("Introduceti consumul aragazului:\t\t", "Consumul")
                e = verificare_digit("Introduceti adancimea aragazului:\t\t", "Adancimea")
                f = verificare_digit("Introduceti latimea aragazului:\t\t\t", "Latimea")
                g = verificare_digit("Introduceti inaltimea aragazului:\t\t", "Inaltimea")
                h = verificare_digit("Introduceti numarul de arzatoare ale aragazului:", "Numarul de arzatoare")
                j = len(globals())
                globals()[j] = Aragaz(b, c, a)
                globals()[j].creare_electrocasnic_mare(e, f, g)
                globals()[j].creare_aragaz(h)
                globals()[j].clasa = "electrocasnice mari"
                globals()[j].subclasa = "aragaz"
                print "\nProdusul a fost introdus in inventar cu codul: " + str(len(lista_produse))
            elif pickone.upper() == "Q":  # Pentru intoarcere la meniul anterior
                break
            else:
                print "--------------------------------------------------------\n"
                print "OPTIUNEA INTRODUSA NU ESTE VALIDA.\n".center(56)

    if var == "2":
        while True:
            print "--------------------------------------------------------"
            print "MENIUL CURENT ESTE:".center(56)
            print """
1 - Introducere mixer
2 - Introducere fier de calcat
Q - Pentru intoarcere la meniul anterior\n"""
            pickone = raw_input("Alege o optiune din meniu:\t")
            print "--------------------------------------------------------"
            if pickone == "1":  # Pentru introducere mixer
                print "INTRODUCERE MIXER\n".center(56)
                a = verificare_alpha("Introduceti producatorul mixerului:\t\t", "Numele producatorului")
                b = verificare_digit("Introduceti pretul mixerului:\t\t\t", "Pretul")
                c = verificare_digit("Introduceti consumul mixerului:\t\t\t", "Consumul")
                e = verificare_digit("Introduceti lungimea cablului mixerului:\t", "Lungimea cablului")
                f = verificare_digit("Introduceti bateria mixerului:\t\t\t", "Bateria")
                g = verificare_digit("Introduceti rotatiile pe minut ale mixerului:\t", "Rotatiile pe minut")
                j = len(globals())
                globals()[j] = Mixer(b, c, a)
                globals()[j].creare_electrocasnic_mic(e, f)
                globals()[j].creare_mixer(g)
                globals()[j].clasa = "electrocasnice mici"
                globals()[j].subclasa = "mixer"
                print "\nProdusul a fost introdus in inventar cu codul: " + str(len(lista_produse))
            elif pickone == "2":  # Pentru introducere fier_calcat
                print "INTRODUCERE FIER DE CALCAT\n".center(56)
                a = verificare_alpha("Introduceti producatorul fierului:\t", "Numele producatorului")
                b = verificare_digit("Introduceti pretul fierului:\t\t", "Pretul")
                c = verificare_digit("Introduceti consumul fierului:\t\t", "Consumul")
                e = verificare_digit("Introduceti lungimea cablului fierului:\t", "Lungimea cablului")
                f = verificare_digit("Introduceti bateria produsului:\t\t", "Bateria")
                g = verificare_digit("Introduceti rezervorul fierului:\t", "Rezervorul")
                j = len(globals())
                globals()[j] = Fier_calcat(b, c, a)
                globals()[j].creare_electrocasnic_mic(e, f)
                globals()[j].creare_fier_calcat(g)
                globals()[j].clasa = "electrocasnice mici"
                globals()[j].subclasa = "fier de calcat"
                print "\nProdusul a fost introdus in inventar cu codul: " + str(len(lista_produse))
            elif pickone.upper() == "Q":  # Pentru intoarcere la meniul anterior
                break
            else:
                print "--------------------------------------------------------\n"
                print "OPTIUNEA INTRODUSA NU ESTE VALIDA.\n".center(56)


def afisare_subclase():
    """Prima parte din procedura de afisare a unei subclase"""
    while True:
        print "--------------------------------------------------------"
        print "MENIUL CURENT ESTE:".center(56)
        print """
1 - Afisare electrocasnice mari
2 - Afisare electrocasnice mici
Q - Pentru intoarcere la meniul anterior\n"""
        pickone = raw_input("Alege o optiune din meniu:\t")
        if pickone == "1":  # Afisare electrocasnice mari
            afisare_subclase1("1")
        elif pickone == "2":  # Afisare electrocasnic mici
            afisare_subclase1("2")
        elif pickone.upper() == "Q":  # Pentru intoarcere la meniul anterior
            break
        else:
            print "--------------------------------------------------------\n"
            print "OPTIUNEA INTRODUSA NU ESTE VALIDA.\n".center(56)


def afisare_subclase1(var):
    """A doua parte din procedura de afisare a unei subclase"""
    if var == "1":
        while True:
            print "--------------------------------------------------------"
            print "MENIUL CURENT ESTE:".center(56)
            print """
1 - Afisare toate electrocasnicele mari
2 - Afisare frigidere
3 - Afisare aragazuri
Q - Pentru intoarcere la meniul anterior\n"""
            pickone = raw_input("Alege o optiune din meniu:\t")
            if pickone == "1":  # Pentru afisare electrocasnice mari
                print "--------------------------------------------------------"
                i = 0
                for e in lista_produse:
                    if e.clasa == "electrocasnice mari":
                        i += 1
                if i == 0:
                    print "\n"
                    print "CATALOGUL NU CONTINE ELECTROCASNICE MARI IN ACEST MOMENT.\n".center(56)
                else:
                    print "ELECTROCASNICE MARI DIN CATALOG\n".center(56)
                i = 1
                for e in lista_produse:
                    if e.clasa == "electrocasnice mari":
                        print "PRODUSUL " + str(i)
                        afisare(e)
                        i += 1

            if pickone == "2":  # Pentru afisare frigidere
                print "--------------------------------------------------------"
                i = 0
                for e in lista_produse:
                    if e.subclasa == "frigider":
                        i += 1
                if i == 0:
                    print "\n"
                    print "CATALOGUL NU CONTINE FRIGIDERE IN ACEST MOMENT.\n".center(56)
                else:
                    print "FRIGIDERE DIN CATALOG\n".center(56)
                i = 1
                for e in lista_produse:
                    if e.subclasa == "frigider":
                        print "PRODUSUL " + str(i)
                        afisare(e)
                        i += 1

            elif pickone == "3":  # Pentru afisare aragazuri
                print "--------------------------------------------------------"
                i = 0
                for e in lista_produse:
                    if e.subclasa == "aragaz":
                        i += 1
                if i == 0:
                    print "\n"
                    print "CATALOGUL NU CONTINE ARAGAZURI IN ACEST MOMENT.\n".center(56)
                else:
                    print "ARAGAZURI DIN CATALOG\n".center(56)
                i = 1
                for e in lista_produse:
                    if e.subclasa == "aragaz":
                        print "PRODUSUL " + str(i)
                        afisare(e)
                        i += 1

            elif pickone.upper() == "Q":  # Pentru intoarcere la meniul anterior
                break
            elif pickone not in ("1", "2", "3", "Q"):
                print "--------------------------------------------------------\n"
                print "OPTIUNEA INTRODUSA NU ESTE VALIDA.\n".center(56)

    if var == "2":
        while True:
            print "--------------------------------------------------------"
            print "MENIUL CURENT ESTE:".center(56)
            print """
1 - Afisare toate electrocasnicele mici
2 - Afisare mixere
3 - Afisare fiare de calcat
Q - Pentru intoarcere la meniul anterior\n"""
            pickone = raw_input("Alege o optiune din meniu:\t")
            if pickone == "1":  # Pentru afisare electrocasnice mici
                print "--------------------------------------------------------"
                i = 0
                for e in lista_produse:
                    if e.clasa == "electrocasnice mici":
                        i += 1
                if i == 0:
                    print "\n"
                    print "CATALOGUL NU CONTINE ELECTROCASNICE MICI IN ACEST MOMENT.\n".center(56)
                else:
                    print "ELECTROCASNICE MICI DIN CATALOG\n".center(56)
                i = 1
                for e in lista_produse:
                    if e.clasa == "electrocasnice mici":
                        print "PRODUSUL " + str(i)
                        afisare(e)
                        i += 1

            if pickone == "2":  # Pentru afisare mixere
                print "--------------------------------------------------------"
                i = 0
                for e in lista_produse:
                    if e.subclasa == "mixer":
                        i += 1
                if i == 0:
                    print "\n"
                    print "CATALOGUL NU CONTINE MIXERE IN ACEST MOMENT.\n".center(56)
                else:
                    print "MIXERE DIN CATALOG\n".center(56)
                i = 1
                for e in lista_produse:
                    if e.subclasa == "mixer":
                        print "PRODUSUL " + str(i)
                        afisare(e)
                        i += 1

            elif pickone == "3":  # Pentru afisare fiare de calcat
                print "--------------------------------------------------------"
                i = 0
                for e in lista_produse:
                    if e.subclasa == "fier de calcat":
                        i += 1
                if i == 0:
                    print "\n"
                    print "CATALOGUL NU CONTINE FIARE DE CALCAT IN ACEST MOMENT.\n".center(56)
                else:
                    print "FIARE DE CALCAT DIN CATALOG\n".center(56)
                i = 1
                for e in lista_produse:
                    if e.subclasa == "fier de calcat":
                        print "PRODUSUL " + str(i)
                        afisare(e)
                        i += 1
            elif pickone.upper() == "Q":  # Pentru intoarcere la meniul anterior
                break
            elif pickone not in ("1", "2", "3", "Q"):
                print "--------------------------------------------------------\n"
                print "OPTIUNEA INTRODUSA NU ESTE VALIDA.\n".center(56)


# Initializare obiect 1 de tip Frigider
frigider1 = Frigider("1149", "267", "ARCTIC")
frigider1.creare_electrocasnic_mare("60", "54", "181")
frigider1.creare_frigider("87", "204")
frigider1.clasa = "electrocasnice mari"
frigider1.subclasa = "frigider"

# Initializare obiect 2 de tip Frigider
frigider2 = Frigider("2099", "280", "SAMSUNG")
frigider2.creare_electrocasnic_mare("66", "59", "185")
frigider2.creare_frigider("98", "223")
frigider2.clasa = "electrocasnice mari"
frigider2.subclasa = "frigider"

# Initializare obiect 3 de tip Aragaz
aragaz1 = Aragaz("1055", "59", "BRAUN")
aragaz1.creare_electrocasnic_mare("60", "60", "85")
aragaz1.creare_aragaz("4")
aragaz1.clasa = "electrocasnice mari"
aragaz1.subclasa = "aragaz"

# Initializare obiect 4 de tip Aragaz
aragaz2 = Aragaz("649", "62", "HOTPOINT")
aragaz2.creare_electrocasnic_mare("50", "50", "85")
aragaz2.creare_aragaz("3")
aragaz2.clasa = "electrocasnice mari"
aragaz2.subclasa = "aragaz"

# Initializare obiect 5 de tip Mixer
mixer1 = Mixer("110", "200", "ARCTIC")
mixer1.creare_electrocasnic_mic("2", "150")
mixer1.creare_mixer("1000")
mixer1.clasa = "electrocasnice mici"
mixer1.subclasa = "mixer"

# Initializare obiect 6 de tip Mixer
mixer2 = Mixer("150", "250", "HOTPOINT")
mixer2.creare_electrocasnic_mic("2", "160")
mixer2.creare_mixer("1050")
mixer2.clasa = "electrocasnice mici"
mixer2.subclasa = "mixer"

# Initializare obiect 7 de tip Fier calcat
fiercalcat1 = Fier_calcat("250", "2400", "SAMSUNG")
fiercalcat1.creare_electrocasnic_mic("3", "1200")
fiercalcat1.creare_fier_calcat("900")
fiercalcat1.clasa = "electrocasnice mici"
fiercalcat1.subclasa = "fier de calcat"

# Initializare obiect 8 detip Fier calcat
fiercalcat2 = Fier_calcat("250", "2300", "BRAUN")
fiercalcat2.creare_electrocasnic_mic("3", "1500")
fiercalcat2.creare_fier_calcat("950")
fiercalcat2.clasa = "electrocasnice mici"
fiercalcat2.subclasa = "fier de calcat"

while True:
    print "--------------------------------------------------------"
    print "MENIUL CURENT ESTE:".center(56)
    print """
1 - Afisare lista de produse
2 - Sortare lista de produse dupa pret
3 - Sortare lista de produse dupa consum
4 - Afisare lista de produse dupa producator
5 - Afisare lista de produse dintr-o subclasa
6 - Introducere produs
Q - Pentru iesire\n"""
    pickone = raw_input("Alege o optiune din meniu:\t")
    if pickone == "1":  # Afisare lista de produse
        aragaz1.afisare()
    elif pickone == "2":  # Sortare lista de produse dupa pret
        aragaz1.sortare_pret()
    elif (pickone == "3"):  # Sortare lista de produse dupa consum
        aragaz1.sortare_consum()
    elif (pickone == "4"):  # Afisare lista de produse dupa producator
        print "--------------------------------------------------------"
        picktwo = raw_input("Introduceti numele producatorului dupa care doriti sa sortati produsele: ")
        print "\n"
        aragaz1.sortare_producator(picktwo.upper())
    elif (pickone == "5"):  # Afisare lista de produse dintr-o subclasa
        afisare_subclase()
    elif (pickone == "6"):  # Introducere produs
        introducere_produs()
    elif pickone.upper() == "Q":  # Pentru iesire
        break
    elif pickone not in ("1", "2", "3", "4", "5", "6", "Q"):
        print "--------------------------------------------------------\n"
        print "OPTIUNEA INTRODUSA NU ESTE VALIDA.\n".center(56)
