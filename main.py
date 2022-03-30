import random
import string
import hashlib


def powByMod(num: int, power: int, mod: int):
    ans = 1
    while power > 0:
        if power % 2 == 1:
            ans *= num
            ans %= mod
        num *= num
        num %= mod
        power >>= 1
    return ans


def gcd(k: int, q: int):
    if k == 0:
        return q, 0, 1
    dd, x1, y1 = gcd(q % k, k)
    x = y1 - (q // k) * x1
    y = x1
    return dd, x, y


def findNod(k: int, q: int):
    nod, c1, c2 = gcd(k, q)
    if nod != 1:
        print('Error')
    return c1


def genKey():
    q = 140990220132661942094353836270106675983065715626747592141413983992936990059339
    R = random.randint(0, q // 2) * 2
    p = q * R + 1
    while powByMod(2, q * R, p) != 1 or powByMod(2, R, p) == 1:
        R = random.randint(2, q * 2) * 2
        p = q * R + 1
    x = random.randint(0, p - 1)
    g = powByMod(x, R, p)
    while g == 1:
        x = random.randint(2, p - 1)
        g = powByMod(x, R, p)
    d = random.randint(0, q - 1)
    e = powByMod(g, d, p)
    return p, q, g, e, d


def makeSign(p: int, q: int, g: int, d: int, M: string):
    m = int(hashlib.sha256(M.encode()).hexdigest(), 16)
    k = random.randint(1, q - 1)
    r = powByMod(g, k, p)
    s = findNod(k, q) * (m - d * r) % q
    return r, s


def verifyKey(p: int, q: int, g: int, e: int, M: string, r: int, s: int):
    if not 1 <= r <= (p - 1) or not 0 <= s <= (q - 1):
        return False
    m = int(hashlib.sha256(M.encode()).hexdigest(), 16)
    if (powByMod(e, r, p) * powByMod(r, s, p)) % p == powByMod(g, m, p):
        return True
    else:
        return False


def writeToFile(filename, mode, p, q, g, e, d, r, s, ch, flag):
    file = open(filename, mode)
    if ch == 1:
        file.write('p = ' + str(p) + '\n' + 'q = ' + str(q) + '\n' + 'g = ' + str(g) + '\n' + 'e = ' + str(
            e) + '\n' + 'd = ' + str(d))
    elif ch == 2:
        file.write('r = ' + str(r) + '\n' + 's = ' + str(s))
    elif ch == 3:
        file.write('flag = ' + str(flag))
    file.close()


def main():
    print('Program start!')
    while True:
        print('Choice the operation:\n1 - Gen\n2 - Sign\n3 - Verify\n4 - Exit\n')
        print('Enter: ', end='')
        choicePerson = int(input())
        M = "I, Nikita Demedyuk, love MiKOZI"
        p, q, g, e, d = genKey()
        r, s = makeSign(p, q, g, d, M)
        flag = verifyKey(p, q, g, e, M, r, s)
        if choicePerson == 1:
            print('---------------------------------------------------------------------')
            print('p = ' + str(p) + '\n' + 'q = ' + str(q) + '\n' + 'g = ' + str(g) + '\n' + 'e = ' + str(e) + '\n'
                  + 'd = ' + str(d))
            writeToFile('Report.txt', 'w', p, q, g, e, d, r, s, choicePerson, flag)
            print('---------------------------------------------------------------------')
        elif choicePerson == 2:
            print('---------------------------------------------------------------------')
            print('r = ' + str(r) + '\n' + 's = ' + str(s))
            writeToFile('Report.txt', 'w', p, q, g, e, d, r, s, choicePerson, flag)
            print('---------------------------------------------------------------------')
        elif choicePerson == 3:
            print('---------------------------------------------------------------------')
            print('flag = ' + str(flag))
            writeToFile('Report.txt', 'w', p, q, g, e, d, r, s, choicePerson, flag)
            print('---------------------------------------------------------------------')
        elif choicePerson == 4:
            print('---------------------------------------------------------------------')
            print('Exit')
            print('---------------------------------------------------------------------')
            break
    print('End of program')


main()
