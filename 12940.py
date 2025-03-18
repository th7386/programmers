#  최대공약수와 최소공배수

def gcd(a, b):
    return b if a % b == 0 else gcd(b, a % b)


def lcm(a, b):
    return int(a * b / gcd(a, b))


def gcdlcm(a, b):
    return [gcd(a, b), lcm(a, b)]
