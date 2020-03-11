from Manusia import Manusia
    
class Mahasiswa(Manusia):
    """Class Mahasiswa yang dibangun dari class Manusia"""
    def __init__ (self, nama, nim, kota,us, lk=[]):
        self.nama = nama
        self.nim = nim
        self.koting = kota
        self.usak = us
        self.listkuliah = lk
    def __str__ (self):
        s = self.nama + ', NIM '+ str(self.nim)\
            + ', Tinggal di '+ self.koting \
            + ', Uang Saku ' +str(self.usak)\
            +', tiap bulannya.'
        return s
    def ambilNama(self):
        return self.nama
    def ambilNIM(self):
        return self.nim
    def ambilUangSaku(self):
        return self.usak
    def makan(self, d):
        print ('Saya baru saja makan' , d, 'sambil belajar')
        self.keadaan = 'kenyang'
    def ambilKotaTinggal(self):
        return self.koting
    def perbaruiKoTing(self, pindahan):
        self.koting = pindahan
    def tambahUangSaku (self, tambah):
        self.tambah = tambah
        return (self.usak)+(self.tambah)
    def dataMahasiswa(self, data):
        self.data = self.nama + self.nim + self.koting + self.usak
        self.data = input("Masukkan data: ")
    def ambilKuliah(self, ambil):
        self.listkuliah.append(ambil)
    def hapusListKuliah(self, hapus):
        for x in self.listkuliah:
            if hapus in self.listkuliah:
                self.listkuliah.remove(hapus)
            else:
                print("Maaf mata kuliah tidak ada dalam list mata kuliah yang diambil")

        

m1 = Mahasiswa('Ani', 234, 'Bandung',450000)


a = input("Masukkan nama: ")
b = input("Masukkan nim: ")
c = input("Masukkan kota tinggal: ")
d = input("Masukkan uang saku: ")

x = Mahasiswa(a,b,c,d)
print (x)
