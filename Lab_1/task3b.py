def salam():
    print("Salam, Dünya!")


def kub_hesabla(n):
    return n ** 3


def birlesdir(soz1, soz2):
    return f"{soz1} {soz2}"


def cap_et(lst):
    for item in lst:
        print(item)


def toplam(*args):
    return sum(args)


def ortalama(*args):
    if len(args) == 0:
        return "Rəqəm yoxdur"
    return sum(args) / len(args)


def adlar_reqemler(**kwargs):
    for ad, reqem in kwargs.items():
        print(f"ad: {ad}, rəqəm: {reqem}")


def tip_yoxla(deyer):
    if isinstance(deyer, str):
        print("mətn")
    elif isinstance(deyer, (int, float)):
        print("rəqəm")
    else:
        print("başqa")


def yas_kateqoriya():
    yas = int(input("Yaşınızı daxil edin: "))
    if yas < 18:
        print("Gənc")
    else:
        print("Yetkin")


def soz_uzunluq():
    soz = input("Söz daxil edin: ")
    print(len(soz))
