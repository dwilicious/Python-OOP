# Base Class
class orang:
    def __repr__(self):
        return f"<nama depan adalah {self.namadepan} dan nama belakangnya {self.namabelakang} >"

    def __init__(self, fname, lname):
        self.namadepan = fname
        self.namabelakang = lname

    def infoorang(self):
        print(self.namadepan, self.namabelakang)

# Child Class


class presiden(orang):
    def __init__(self, namadepan, namabelakang, yelect):
        super().__init__(namadepan, namabelakang)
        self.terpilih = yelect

    def infopresiden(self):
        print(self.namadepan, self.namabelakang, self.terpilih)


# Test input
y = presiden("Donald", "Trump", "2016")

# Test method inheritance
presiden.infoorang(y)

# Test method child class
presiden.infopresiden(y)
