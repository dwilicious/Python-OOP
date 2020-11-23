# Inheritance

Dalam pemrograman berorientasi objek, inheritance adalah mekanisme mendasarkan objek atau kelas pada objek lain (warisan berbasis prototipe)
atau kelas (warisan berbasis kelas), dengan mempertahankan implementasi serupa. Inheritance juga dapat didefinisikan sebagai penurunan kelas baru (subclass)
dari kelas yang sudah ada seperti super class atau base class dan kemudian membentuknya menjadi hierarki kelas. (wikipedia)

## Inheritance dalam python
### Membuat Class Dasar
Semua class dapat menjadi parent class sehingga membuat parent class di python sama dengan membuat class pada umumnya
contoh:

```python
class orang:
    def __repr__(self):
        return f"<nama depan adalah {self.namadepan} dan nama belakangnya {self.namabelakang} >"

    def __init__(self, fname, lname):
        self.namadepan = fname
        self.namabelakang = lname

    def cetaknama(self):
        print(self.namadepan, self.namabelakang)
```

### Membuat Class Turunan

Misal dibuat class turunan dengan nama class presiden dari class dasar orang. Class presiden mewarisi semua properti class orang

```python
class presiden(orang):
    def __init__(self, namadepan, namabelakang, yelect):
        super().__init__(namadepan, namabelakang)
        self.terpilih = yelect

    def infopresiden(self):
        print(self.namadepan, self.namabelakang, self.terpilih)

```

Class presiden adalah turunan dari Class orang. kita dapat menguji dengan memberikan input data presiden dan menguji metode yang diwarisi *(infoorang)* dengan dibandingkan pada  metode Child Class
*infopresiden*

```python
# Test input
y = presiden("Donald", "Trump", "2016")

# Test method inheritance
presiden.infoorang(y)

# Test method child class
presiden.infopresiden(y)
```
