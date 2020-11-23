class orang:
    def __init__(self, nama, usia):
        self._nama = nama
        self._usia = usia

    def cari_usia(self):
        return self._usia

    def set_usia(self, isi_usia):
        if isinstance(isi_usia, int) and isi_usia > 0 and isi_usia < 120:
            self._usia = isi_usia

    def get_name(self):
        return self._nama

    def __str__(self):
        return 'Saudara [' + str(self._nama) + '] berumur ' + str(self._usia)


# test isi nilai
x = orang("Joni", 45)

# set nilai usia tanpa melalui prosedur
x._usia = -3
print("Nilai usia yang tidak logis")
print(x)

# set nilai usia melalui prosedur
x.set_usia(45)
print("Nilai usia yang logis")
print(x)

# coba set nilai usia tidak logis melalui setter
x.set_usia(-8)
print("Nilai usia tetap saat input tidak logis")
print(x)
