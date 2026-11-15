import random
import json
import os
import sys

if getattr(sys, "frozen", False):
    KLASOR = os.path.dirname(sys.executable)
else:
    KLASOR = os.path.dirname(os.path.abspath(__file__))

DOSYA = os.path.join(KLASOR, "bilgiler.json")


Default = {
    "nickname": "",
    "can": 100,
    "seviye": 1,
    "altın": 500,
    "enerji": 100,
}


def yukle():
    veri = dict(Default)
    if os.path.exists(DOSYA):
        try:
            with open(DOSYA, "r", encoding="utf-8") as f:
                veri.update(json.load(f))
        except json.JSONDecodeError:
            pass
    return veri


def kaydet(veri):
    with open(DOSYA, "w", encoding="utf-8") as f:
        json.dump(veri, f, ensure_ascii=False, indent=4)


programi_kapat = False

while not programi_kapat:
    veri = yukle()

    if veri["nickname"] == "":
        veri["nickname"] = input("Lütfen Bir Nickname Girin: ")
        kaydet(veri)
        print("Nickname kaydedildi!\n")

    print("Lukudorus Krallığına Hoşgeldin", veri["nickname"])
    print("Başlangıç Bilgilerin:")
    print("Nickname:", veri["nickname"])
    print("Seviye:", veri["seviye"])
    print("Altın:", veri["altın"])

    while True:
        try:
            ana_secim = int(input(
                "\nNe Yapmak İstersiniz:\n"
                "1-Avlan 2-Dinlen 3-BOSS Savaşı 4-Çıkış\nSeçiminiz: "
            ))
        except ValueError:
            print("Geçersiz Değer Girdiniz")
            continue

        if ana_secim == 1:
            veri["can"] -= random.randint(5, 15)
            if veri["can"] <= 0:
                print("\nÖldünüz, Oyun Bitti.\n")
                kaydet(dict(Default))
                break
            else:
                print("Canınız:", veri["can"])

        elif ana_secim == 2:
            veri["enerji"] += 10
            if veri["enerji"] > 100:
                veri["enerji"] = 100
                print("Enerji 100'den fazla olamaz.")
            print("Enerjiniz:", veri["enerji"])

        elif ana_secim == 3:
            print("BOSS savaşı yakında!")

        elif ana_secim == 4:
            kaydet(veri)
            print("Oyun kaydedildi, görüşürüz!")
            programi_kapat = True
            break

        else:
            print("1 ile 4 arasında bir sayı girin.")
            continue

        kaydet(veri)