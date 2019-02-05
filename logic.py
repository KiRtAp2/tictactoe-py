import settings


def igra():
    plosca, igralec = pripravi_igro()
    while not konec_igre(plosca):
        prikazi_plosco(plosca)
        poteza = dobi_potezo(igralec)
        naredi_potezo(plosca, poteza, igralec)  # TODO: ali je veljavna?
        igralec = zamenjaj_igralca(igralec)
    prikazi_plosco(plosca)
    zmagovalec = konec_igre(plosca)
    if zmagovalec == 'remi':
        print("Izenaceno!")
    else:
        print("Zmagal je igralec {}!".format(zmagovalec))


def pripravi_igro():
    return [[None for _ in range(settings.SIZE)] for _ in range(settings.SIZE)], settings.IGRALEC1


def prikazi_plosco(plosca):
    for i in range(len(plosca)):
        for j in range(len(plosca[0])):
            print(plosca[i][j] if plosca[i][j] else '_', end=' ')
        print()


def preveri_vrstice(plosca):
    for i in range(settings.SIZE):
        j = 1
        igralec = plosca[i][0]
        if not igralec: continue
        while j < settings.SIZE and plosca[i][j] == igralec:
            j += 1
        if j == settings.SIZE:  # cela vrstica ima isti znak
            return igralec
    return False


def preveri_diagonali(plosca):
    # diagonala levo-desno
    j = 1
    igralec = plosca[0][0]
    while j < settings.SIZE and plosca[j][j] == igralec and igralec:
        j += 1
    if j == settings.SIZE:
        return igralec
    # diagonala desno-levo
    j = 1
    igralec = plosca[0][settings.SIZE-1]
    while j < settings.SIZE and plosca[j][settings.SIZE-1-j] == igralec and igralec:
        j += 1
    if j == settings.SIZE:
        return igralec
    return False


def plosca_je_polna(plosca):
    return sum([sum([1 for znak in vrstica if not znak]) for vrstica in plosca]) == 0


def konec_igre(plosca):
    """Ce je konec igre, vrne igralca, ki je zmagal, ce je remi, vrne 'remi', ce pa igre se ni konec, vrne False."""
    # preveri vrstice
    vrstice_konec = preveri_vrstice(plosca)
    if vrstice_konec: return vrstice_konec

    # preveri stolpce
    stolpci_konec = preveri_vrstice(list(zip(*plosca)))  # preveri vrstice transponirane plosce
    if stolpci_konec: return stolpci_konec

    # preveri diagonali
    diagonala_konec = preveri_diagonali(plosca)
    if diagonala_konec: return diagonala_konec

    if plosca_je_polna(plosca): return 'remi'
    return False


def dobi_potezo(igralec):
    while True:
        vnos = input("Na vrsti je igralec {}. Vpisi vrstico(1-{}) in stolpec(1-{}), npr '1 {}': ".format(
         igralec, settings.SIZE, settings.SIZE, settings.SIZE
        ))
        vnos = vnos.split()
        if len(vnos) == 2:
            try:  # ce je uporabnik vnesel znake, ki niso celo stevilo, bomo ujeli error
                i, j = [int(x)-1 for x in vnos]
                if 0 <= i <= settings.SIZE - 1 and 0 <= j <= settings.SIZE - 1:
                    return i, j
            except ValueError:
                pass
        print("Tvoj vnos je neveljaven, poskusi ponovno.")


def naredi_potezo(plosca, poteza, igralec):
    plosca[poteza[0]][poteza[1]] = igralec


def zamenjaj_igralca(igralec):
    return settings.IGRALEC2 if igralec == settings.IGRALEC1 else settings.IGRALEC1
