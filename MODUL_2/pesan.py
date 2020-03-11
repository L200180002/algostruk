class Pesan (object):
    """
    sebuah class bernama pesan.
    untuk memahami konsep class dan object
    """
    def __init__(self, sebuahString):
        self.teks = sebuahString
    def cetakIni(self):
        print(self.teks)
    def cetakPakaiHurufKapital(self):
        print(str.upper(self.teks))
    def cetakPakaiHurufKecil(self):
        print (str.lower(self.teks))
    def jumKar(self):
        return len(self.teks)
    def cetakJumlahKarakterku(self):
        print ('Kalimatku mempunyai', len(self.teks), 'karakter')
    def perbarui (self,stringBaru):
        self.teks = stringBaru
    def apakahTerkandung(self, stringNih):
        if stringNih in self.teks:
            return True
        else:
            return False
    def HitKon(self):
        vokal = 0
        for char in 'aiueoAIUEO':
            if char in vokal:
                vokal+=1
            return len(jumlah)
