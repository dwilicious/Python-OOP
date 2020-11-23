class akun:
    """
    Rekening klien bank.
    """

    def __repr__(self):
        return f"<Akun {self.name} memiliki {self.saldo} >"

    def __init__(self, pemilik, saldo=0):
        self.name = pemilik
        self.saldo = saldo

    def deposit(self, jumlah):
        self.saldo += jumlah

    def penarikan(self, jumlah):
        self.saldo -= jumlah


a = akun('Albert Einstein', 999999)
print(a.name, a.saldo)

a.deposit(200)

print(a.name, a.saldo)

print(a)
