
STEVILO_DOVOLJENIH_NAPAK = 10
PRAVILNA_CRKA = '+'
PONOVLJENA_CRKA = 'o'
NAPACNA_CRKA = '-'
ZMAGA = 'w'
PORAZ = 'x'

class Igra:
    def __init__(self, geslo, crke):
        self.geslo = geslo
        self.crke = crke

    def napacne_crke(self):
        seznam = []
        for crka in self.crke:
            if crka not in self.geslo:
                seznam.append(crka)
        return seznam

    def pravilne_crke(self):
        seznam = []
        for crka in self.crke:
            if crka in self.geslo:
                seznam.append(crka)
        return seznam

    def stevilo_napak(self):
        return len(napacne_crke)

    def zmaga(self):
        for crka in self.geslo:
            if crka not in self.crke:
                return False
        return True


    def poraz(self):
        for crka in self.geslo:
            if crka in self.crke:
                return False
        return True

    def pravilni_del_gesla(self):
        niz = ''
        for crka in self.geslo:
            if crka in self.crke:
                niz += crka + ' '
            else:
                niz += '_ '
        return niz
    

    def nepravilni_ugibi(self):
        niz = ''
        for crka in self.geslo:
            if crka not in self.crke:
                niz += ' '
        return niz


    def ugibaj(self, crka):
        crka = crka.upper
        if crka in self.crke:
            return PONOVLJENA_CRKA
        elif crka not in self.geslo:
            if self.poraz():
                return PORAZ
            else:
                return NAPACNA_CRKA
        else:
            if self.zmaga():
                return ZMAGA
            else:
                return PRAVILNA_CRKA

bazen_besed = []
with open('besede.txt', 'r', encoding = 'utf - 8') as d:
    for vrstica in d:
        bazen_besed.append(vrstica.upper().strip)

def nova_igra():
    return Igra(random.choice(bazen_besed))

#dokoncaj spletni vmesnik:

ZACETEK = 's'
class Vislice:
    def __init__(self):
        self.igre = {}

    def prost_id_igre(self):
        if len(self.igre) == 0:
            return 0
        else:
            return max(self.igra.keys()) + 1

    def nova_igra(self):
        id_igre = self.prost_id_igre()
        igra = nova_igra()
        self.igre[id_igre] = (igra, ZACETEK)
        return id_igre

    def ugibaj(self, id_igre, crka):
        igra = self.igre[id_igre][0]
        poskus = igra.ugibaj(crka)
        self.igre[id_igre] = (igra, poskus)

#spletni vmesnik:
import bottle
import model


vislice = model.Vislice()

@bottle.get('/')
def index():
    return bottle.template('index.tpl')

bottle.run(reloader=True, debug=True)
