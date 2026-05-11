import pandas as pd
import os

dosya_adi = "kayitlar.csv"

if os.path.exists(dosya_adi):
    df = pd.read_csv(dosya_adi)
    kayitlar = df.to_dict("records")
else:
    kayitlar = []

print("📚 Study Mood-Motivation Tracker")

while True:

    ders = input("Hangi derse çalıştın? ")
    sure = int(input("Kaç dakika çalıştın? "))
    mood = int(input("Motivasyon Seviyen (1-10): "))

    yeni_kayit = {
        "Ders": ders,
        "Süre": sure,
        "Motivasyon": mood
    }

    kayitlar.append(yeni_kayit)

    df = pd.DataFrame(kayitlar)
    df.to_csv(dosya_adi, index=False)

    print("✅ Kayıt başarıyla eklendi!")

    devam = input("Başka kayıt eklemek ister misin? evet/hayır: ")

    if devam == "hayır":
        break

print("\n--- Günlük Çalışma Özeti ---")

toplam_sure = 0

for i in range(len(kayitlar)):

    print(
        kayitlar[i]["Ders"],
        "-",
        kayitlar[i]["Süre"],
        "dakika",
        "| Motivasyon:",
        kayitlar[i]["Motivasyon"]
    )

    toplam_sure += kayitlar[i]["Süre"]

print("\nToplam çalışma süresi:", toplam_sure, "dakika")

if toplam_sure >= 180:
    print("🔥 Harika! Bugün çok verimli çalıştın.")

elif toplam_sure >= 90:
    print("✨ Güzel çalışmışsın, devam et!")

else:
    print("📌 Biraz daha çalışabilirsin.")