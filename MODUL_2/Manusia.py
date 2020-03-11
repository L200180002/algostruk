from datetime import date
class Manusia(object):
    """Class 'Manusia' dengan inisiasi 'nama' """
    keadaan = 'lapar'
    def __init__ (self, nama):
        self.nama = nama
    def ucapkanSalam (self):
        print('Salam, Namaku', self.nama)
    def makan(self,a):
        print('saya baru saja makan ', a)
        self.keadaan = 'kenyang'
    def olahraga (self, b):
        print('Saya baru saja latihan', b)
        self.keadaan = 'lapar'
    def mengalikanDenganDua (selF,c):
        return c*2
    
class SiswaSMA(Manusia):
    def __init__(self, nama, NIS, umur, us):
        """Metode inisiasi ini menutupi metode inisiasi di class Manusia"""
        self.nama = nama
        self.nis = NIS
        self.umur = umur
        self.us = us
        
    def __str__(self):
        s = self.nama +', NIS '+str(self.nis)\
            +'. Berumur '+ str(self.umur) \
            +'. Uang saku Rp. '+ str(self.us)\
            +' tiap harinya.'
        return s

    def tahunlahir(self):
        thnskr = date.today().year
        tl = thnskr - self.umur

p1 = Manusia('Fatimah')
p1.ucapkanSalam()

