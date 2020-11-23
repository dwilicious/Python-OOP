# Enkapsulasi

Enkapsulasi yaitu kemampuan untuk menyembunyikan data di dalam suatu objek dan hanya membatasi akses serta modifikasi obyek melalui gateway ke dalam data tersebut. 
Gateways ini adalah metode yang ditentukan untuk mendapatkan atau menyetel nilai atribut (sering disebut sebagai getter dan setter). 
Enkapsulasi memungkinkan lebih banyak kontrol atas akses ke data; penggunaannya misal untuk memeriksa validitas data usia, dengan memeriksa hanya 
bilangan bulat positif di atas nol, tetapi di bawah 120.

Python tidak secara eksplisit memiliki konsep enkapsulasi; tetapi hanya bergantung pada dua hal yaitu; 
1. konvensi standar yang digunakan untuk menunjukkan bahwa atribut harus dianggap privat
2. konsep yang disebut properti yang memungkinkan penyetel dan pengambil ditentukan untuk atribut.

Semua atribut objek tersedia untuk umum dalam Python; artinya, semuanya atribut terlihat oleh kode apa pun yang menggunakan objek. 
Untuk menunjukkan bahwa sebuah obyek bersifat privat digunakan awalan karakter underbar ('_') pada nama atribut seperti yang ditunjukkan di bawah ini:

```python
class orang:
    def __init__(self, nama, usia):
        self._nama = nama
        self._usia = usia

    def cari_usia(self):
        return self._usia

    def set_usia(self, isi_usia):
        if isinstance(isi_usia, int) and isi_usia > 0 and isi_usia < 120:
            self._usia = isi_usia

    def cari_nama(self):
        return self._nama

    def __str__(self):
        return 'Saudara [' + str(self._nama) + '] berumur ' + str(self._usia)
```

Pada kode di atas diberitahukan bahwa nama dan usia bersifat privat. Namun hal tersebut hanya berupa konvensi sehingga jika dilakukan perubahan
nilai usia secara tidak logis dengan kode

```python
x._usia = -5
```

maka nilai usia tetap bernilai -5 yang tidak masuk akal berdasar konteks kode program.

Untuk mengakses nama dan usia secara masuk akal, disediakan gateway berupa metode *getter* dan *setter*. Dalam kode program di atas metode *getter* adalah
*cari_nama* dan *cari_usia* sedangkan metode *sette*r adalah *set_usia*.
Pada metode *setter set_usia* dapat dilakukan validasi dimana jika nilai usia berada diantara 1 sampai 120 maka dilakukan update pada usia, jika hal tersebut tidak terpenuhi
maka tidak dilakukan update nilai usia.
