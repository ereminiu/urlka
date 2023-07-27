from random import randint
from random import shuffle

class Encrypter:
    def __init__(self) -> None:
        self.CODELEN = 7

    def get_sold(self) -> str:
        sold = ""
        for _ in range(randint(100, 555)):
            start_with = 'a'
            if randint(0, 1) % 2:
                start_with = 'A'
            sold += chr(ord(start_with) + randint(0, 25))
        return sold
    
    def get_hash(self, s: str) -> int:
        s_array = [c for c in s]
        shuffle(s_array)
        s = str(s_array)
        mod = int(1e7)
        base = 37
        res = 0
        for c in s:
            res = (res * base + ord(c) + 1) % mod
        return res
    
    def encrypt_int(self, x: int) -> str:
        code = ''
        digits = 0
        if randint(1, 3) < 3 or digits == 3:
            code = ord('a') + x
            if randint(0, 1) % 2 == 0:
                code += ord('A') - ord('a')
        else:
            code = ord('0') + x
            digits += 1
        return chr(code)

    def get_code(self, link: str) -> str:
        s = self.get_sold() + link + self.get_sold()
        hash = self.get_hash(s)
        res = ""
        while hash > 0: 
            res += self.encrypt_int(hash % 10)
            hash //= 10
        # check whether len(res) < CODELEN
        extra = self.CODELEN - len(res)
        for _ in range(extra):
            res += self.encrypt_int(randint(1, 10))
        return res