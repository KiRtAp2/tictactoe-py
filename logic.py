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
