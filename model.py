
STEVILO_DOVOLJENIH_NAPAK = 10
PRAVILNA_CRKA = '+'
PONOVLJENA_CRKA = 'o'
NAPACNA_CRKA = '-'
ZMAGA = 'w'
PORAZ = 'x'

class Igra:
    def __init__(self, geslo, crke:
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


    def ugibaj(crka):
        