# Polimorfisme dengan fungsi dan obyek
class harimau():
    def jenis(self):
        print("Peliharaan")

    def diet(self):
        print("Carnivora")


class kijang():
    def jenis(self):
        print("Liar")

    def diet(self):
        print("Herbivora")


class beruang():
    def jenis(self):
        print("Liar")

    def diet(self):
        print("Omnivora")


def func(obj):
    obj.jenis()
    obj.diet()


obj_harimau = harimau()
obj_kijang = kijang()
obj_beruang = beruang()

func(obj_harimau)
func(obj_kijang)
func(obj_beruang)


# Polimorfisme dengan Class Method
class jawa_tengah():
    def ibukota(self):
        print("Semarang")

    def kuliner(self):
        print("Tahu Gimbal")


class maluku():
    def ibukota(self):
        print("Ambon")

    def kuliner(self):
        print("Nasi Kelapa")


obj_ind = jawa_tengah()
obj_usa = maluku()

for propinsi in (obj_ind, obj_usa):
    propinsi.ibukota()
    propinsi.kuliner()


# Polymorfisme dengan Inheritance
class burung:
    def awalan(self):
        print("Terdapat bermacam-macam burung")

    def terbang(self):
        print("Kebanyakan burung dapat terbang, tetapi beberapa tidak")


class merpati(burung):
    def terbang(self):
        print("Merpati dapat terbang")


class ayam(burung):
    def terbang(self):
        print("Ayam tidak dapat terbang")


obj_burung = burung()
obj_merpati = merpati()
obj_ayam = ayam()

obj_burung.awalan()
obj_burung.terbang()

obj_merpati.awalan()
obj_merpati.terbang()

obj_ayam.awalan()
obj_ayam.terbang()
