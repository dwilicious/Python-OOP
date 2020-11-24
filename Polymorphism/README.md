# Polimorfisme

## Definisi
Polimorfisme dapat diartikan kemampuan untuk mengambil bentuk yang berbeda. 
Polimorfisme dalam Python memungkinkan kita untuk mendefinisikan metode di kelas anak dengan nama yang sama seperti yang didefinisikan di kelas induknya. 
Class anak mewarisi semua metode dari Class induk. Namun, dalam beberapa situasi, metode yang diwarisi dari Class induk kurang cocok dengan Class anak. 
Dalam kasus seperti itu, harus diimplemtasikan kembali metode di kelas anak. Ada beberapa implementasi metode polimorfisme seperti penggunaan fungsi, metode class atau obyek yang 
berbeda.

## Polimorfisme dengan fungsi dan obyek
Suatu fungsi dapat dibuat untuk dapat mengambil objek apa pun, sehingga memungkinkan terjadinya polimorfisme.
Misal sebuah fungsi bernama "func()" yang akan mengambil sebuah objek yang akan kita beri nama "obj". 
Dalam hal ini, metode jenis() dan diet(), yang masing-masing didefinisikan dalam tiga kelas yaitu 'harimau', 'kijang' dan 'Beruang'. 

```python
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
```
Ketika obyek diberikan pada fungsi maka output yang keluar akan berbeda sesuai metode pada masing-masing obyek sebagai berikut:
```
Peliharaan
Carnivora
Liar
Herbivora
Liar
Omnivora
```

## Polymorfisme dengan method class

```python
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
```

## Polimorfisme dengan Inheritance
```python
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
```
