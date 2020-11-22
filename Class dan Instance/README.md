Apakah class itu?

Dalam pemrograman berorientasi objek, class adalah cetak biru untuk membuat objek. Class menentukan apa yang dimiliki sebuah objek (atribut) dan apa yang dapat dilakukan objek (metode). Umumnya Class mewakili sebuah kata benda yang dapat merupakan seseorang, hewan, buah, ataupun benda mati. Contohnya adalah kelas Pegawai. Kelas Pegawai mempunyai atribut berupa nama, usia, dan jenis kelamin serta memiliki metode bekerja. (wikipedia indonesia)

Class digunakan untuk mengelola kompleksitas, sehingga program utama menjadi lebih sederhana.
Contoh cara menggunakan class

Mendefinisikan class
Untuk menentukan class, Anda perlu mendefinisikan tiga hal:
-beri nama class
-definisikan atribut (variabel yang dimiliki class)
-definisikan metode (fungsi yang dimiliki class)

Dalam kode di bawah ini, class untuk akun rekening bank dapat disusun sebagai berikut:

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

Akun class berisi dua atribut (nama pemilik dan saldo) dan dua metode (setoran dan penarikan).

Membuat Objek
Untuk menggunakan class, Anda perlu membuat objek dari class terlebih dahulu. Objek adalah "versi langsung" dari sebuah class. Dapat dibuat perandaian jika Anda menganggap Manusia sebagai sebuah class, maka Albert Einstein dan Leonardo da Vinci adalah contoh objek.

Anda dapat membuat beberapa objek dari sebuah class, dan setiap objek memiliki atributnya sendiri-sendiri (misalnya jika class Manusia memiliki atribut usia, maka usia Enstein dan Leonardo mungkin berbeda).

Untuk membuat objek Akun Rekening Bank, Anda perlu memanggil class. Membuat objek secara otomatis akan memanggil konstruktor **init**(self) dengan parameter yang disediakan.

misal:
a = Akun ('Albert Einstein', 999999)
m = Akun ('Leonardo da Vinci', 666666)

Kemudian Anda dapat mengakses atribut seperti variabel menggunakan sintaks titik (.):

print (a.pemilik)
print (m.saldo)

Dan Anda dapat mengakses metode dengan cara yang serupa:

a.setor (100)
a.penarikan (10)
print(a.balance)

Penggunaan metode tersebut mengubah status objek akun Einstein, tetapi tidak merubah status Leonardo.

Membuat class dapat dicetak
Salah satu kelemahan class adalah ketika Anda mencetak sebuah objek, Anda akan melihat sesuatu seperti ini:

:::pesta
<** main **. Akun di 0x7f64519d8438>
Solusi yang baik adalah dengan menambahkan metode khusus, **repr ** (self) ke class yang mengembalikan string. Metode ini akan dipanggil setiap kali representasi string diperlukan: saat mencetak dan objek, saat objek muncul di dalam daftar atau dalam pesan kesalahan.

Biasanya, Anda akan membuat string pendek di **repr ** (self) yang mendeskripsikan objek:

::: python3
def **repr ** (sendiri):
kembalikan f "<Akun '{self.name}' dengan kredit galaksi {self.balance}>"
Dengan metode ini didefinisikan, instruksi

::: python3
cetak (a)
akan menghasilkan keluaran

:::pesta
<Akun 'Ada Lovelace' dengan 1324 kredit galaksi> "
Ide yang bagus untuk mengimplementasikan **repr ** (self) sebagai metode pertama di class baru.

Peringatan
Dalam bahasa pemrograman lain class sering diiklankan untuk "memodelkan objek dunia nyata atau entitas logis". Ini sebagian benar dengan Python. Perhatikan bahwa Python menawarkan banyak alternatif untuk menggunakan class, mis. kamus, tuple bernama atau DataFrames mungkin sering memiliki tujuan yang sama dengan baik.

Motivasi lain untuk menggunakan class yang Anda temukan di buku teks adalah enkapsulasi, memisahkan bagian dari program Anda dari yang lain. Enkapsulasi tidak ada dalam Python (mis. Anda tidak dapat mendeklarasikan bagian class sebagai privat dengan cara yang tidak dapat dielakkan). Jika Anda bergantung pada kode Anda yang diisolasi secara ketat dari bagian lain (misalnya dalam aplikasi keamanan kritis atau saat mengatur program yang sangat besar), pertimbangkan bahasa pemrograman lain selain Python.
