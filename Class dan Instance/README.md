# Apa itu class?

Dalam pemrograman berorientasi objek, class adalah cetak biru untuk membuat objek. Class menentukan apa yang dimiliki sebuah objek (atribut) dan apa yang dapat dilakukan objek (metode). Umumnya Class mewakili sebuah kata benda yang dapat merupakan seseorang, hewan, buah, ataupun benda mati. Contohnya adalah kelas Pegawai. Kelas Pegawai mempunyai atribut berupa nama, usia, dan jenis kelamin serta memiliki metode bekerja. (wikipedia indonesia)

Class digunakan untuk mengelola kompleksitas, sehingga program utama menjadi lebih sederhana.
Contoh cara menggunakan class

## Mendefinisikan class

Untuk menentukan class, Anda perlu mendefinisikan tiga hal:
-beri nama class
-definisikan atribut (variabel yang dimiliki class)
-definisikan metode (fungsi yang dimiliki class)

Dalam kode di bawah ini, class untuk akun rekening bank dapat disusun sebagai berikut:

```python
class akun:
"""
Rekening klien bank.
"""

    def __init__(self, pemilik, saldo=0):
        self.name = pemilik
        self.saldo = saldo

    def setor(self, jumlah):
        self.saldo += jumlah

    def penarikan(self, jumlah):
        self.saldo -= jumlah
```

Akun class berisi dua atribut (nama pemilik dan saldo) dan dua metode (setoran dan penarikan).

Membuat Objek
Untuk menggunakan class, Anda perlu membuat objek dari class terlebih dahulu. Objek adalah "versi langsung" dari sebuah class. Dapat dibuat perandaian jika Anda menganggap Manusia sebagai sebuah class, maka Albert Einstein dan Leonardo da Vinci adalah contoh objek.

Anda dapat membuat beberapa objek dari sebuah class, dan setiap objek memiliki atributnya sendiri-sendiri (misalnya jika class Manusia memiliki atribut usia, maka usia Enstein dan Leonardo mungkin berbeda).

Untuk membuat objek Akun Rekening Bank, Anda perlu memanggil class. Membuat objek secara otomatis akan memanggil konstruktor **init**(self) dengan parameter yang disediakan.

misal:
a = Akun ('Albert Einstein', 999999)

l = Akun ('Leonardo da Vinci', 666666)

Kemudian Anda dapat mengakses atribut seperti variabel menggunakan sintaks titik (.):
```python
print (a.pemilik)
print (m.saldo)
```
Dan Anda dapat mengakses metode dengan cara yang serupa:
```python
a.setor (100)
a.penarikan (10)
print(a.balance)
```
Penggunaan metode tersebut mengubah status objek akun Einstein, tetapi tidak merubah status Leonardo.

## Membuat class dapat dicetak

Salah satu kelemahan class adalah ketika Anda mencetak sebuah objek, Anda akan melihat sesuatu seperti ini:
```python
<class '**main**.akun'>
```
Solusinya adalah dengan menambahkan metode khusus, **repr**(self) ke class yang mengembalikan string. Metode ini akan dipanggil setiap kali representasi string diperlukan: saat mencetak dan objek, saat objek muncul di dalam daftar atau dalam pesan error.

Biasanya, Anda akan membuat string pendek di **repr**(self) yang mendeskripsikan objek:
```python
def **repr**(self):
return f"<Akun {self.name} memiliki {self.saldo} >"
```
Dengan penambahan metode tersebut maka saat dilakukan operasi pencetakan obyek akan menghasilkan keluaran berupa string

```python
print (a)
output:
<Akun Albert Einstein memiliki 1000199 >
```

Mengimplementasikan **repr**(self) sebagai metode pertama di class baru dapat menjadi pertimbangan untuk jika ingin menghasilkan keluaran string.

Dalam bahasa pemrograman lain class sering digunakan untuk "memodelkan objek dunia nyata atau entitas logis". Hal tersebut bukan satu-satunya fungsi class di Python karena banyak alternatif untuk penggunaan class lainyya, misal sebagai dictionary, named tuple atau DataFrames.

Kasus lain dalam menggunakan class adalah enkapsulasi, yaitu memisahkan bagian dari program dengan bagian yang lain yang akan dibahas di bagian lain.
