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


def prikazi_plosco(plosca):
    for i in range(len(plosca)):
        for j in range(len(plosca[0])):
            print(plosca[i][j] if plosca[i][j] else '_', end=' ')
        print()
