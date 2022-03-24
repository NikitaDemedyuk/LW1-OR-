import random
import string
import hashlib


def gcd(k: int, q: int):
    if k == 0:
        return q, 0, 1
    d, x1, y1 = gcd(q % k, k)
    x = y1 - (q // k) * x1
    y = x1
    return x


def generateKey(k, int, q: int):
    nod, c1, c2 = gcd(k, q)
    if nod != 1:
        print('Error')
    return c1


def genKey():
    q = 140990220132661942094353836270106675983065715626747592141413983992936990059339
    print('q = ' + str(q))
    R = random.randint(0, q // 2) * 2
    p = q * R + 1
    print('R = ' + str(R) + '\n')
    while 2 ** (q * R) % p != 1 or 2 ** R % p == 1:
        R = random.randint(0, q // 2) * 2
        p = q * R + 1
        print('R = ' + str(R) + '\n')
    x = random.randint(0, p)
    g = (x ** R) % p
    while g == 1:
        x = random.randint(0, p)
        g = (x ** R) % p
    print('g = ' + str(g))
    d = random.randint(0, q)
    e = g ** d % p
    return p, q, g


def makeSign(p: int, q: int, g: int, d: int, M: string):
    m = int(hashlib.sha256(M.encode()).hexdigest(), 16)
    k = random.randint(1, q)
    r = (g ** k) % p


def main():
    genKey()


main()
