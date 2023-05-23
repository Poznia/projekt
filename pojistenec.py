class Pojistenec():
    jmeno = None
    prijmeni = None
    vek = 1
    telcislo = 1

    def __init__(self, jmeno, prijmeni, vek, telcislo):
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.vek = vek
        self.telcislo = telcislo

    def __str__(self):
        return self.jmeno

