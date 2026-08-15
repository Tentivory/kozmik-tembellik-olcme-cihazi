#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Kozmik Tembellik Ölçme Cihazı v1.0
Resmi, bilimsel, hiç de şaka değil bir tembellik analiz sistemi.
Kullanmadan önce derin bir nefes alın ve hiçbir şey yapmayın.
"""

import random
import time
from datetime import datetime

def abartili_yukle():
    print("\n" + "="*60)
    print("  KOZMİK TEMBELLİK ÖLÇME CİHAZI BAŞLATILIYOR...")
    print("  Lütfen bekleyiniz. Acele etmeyiniz. Zaten etmiyorsunuz.")
    print("="*60)
    for i in range(5):
        time.sleep(0.4)
        print(f"  Sistem yükleniyor... {'.' * (i+1)}")
    print("\n  Yükleme tamamlandı. Artık tembellik ölçebilirsiniz.\n")

def tembellik_hesapla():
    print("Lütfen aşağıdaki soruları samimi bir şekilde cevaplayınız.")
    print("(Yalan söylemek tembellik puanınızı artırır, biz de tembeliz.)\n")
    
    try:
        uyku = float(input("Bugün kaç saat uyudunuz? (0-24): ") or 8)
        ertelenen = int(input("Kaç işi ertelediniz? (sayı): ") or 3)
        kahve = int(input("Kaç fincan kahve içtiniz ama hala yorgunsunuz? : ") or 2)
        telefon = int(input("Telefonu kaç kez gereksiz yere kontrol ettiniz? : ") or 47)
    except:
        print("\nHata: Sayısal değer girmediniz. Bu da bir tembellik belirtisidir.")
        uyku, ertelenen, kahve, telefon = 12, 7, 5, 99

    # Absürt formül
    baz_puan = (uyku * 3.14) + (ertelenen * 7.77) + (kahve * 2.5) + (telefon * 0.13)
    rastgele_kozmik_faktor = random.uniform(0.8, 1.4)
    tembellik_indeksi = baz_puan * rastgele_kozmik_faktor

    # Seviye belirleme
    if tembellik_indeksi < 30:
        seviye = "Şüpheli Aktif"
        yorum = "Bir şeyler yapıyorsunuz gibi. Bu cihaz sizi anlamıyor. Yeniden ölçün."
    elif tembellik_indeksi < 70:
        seviye = "Orta Seviye Tembel"
        yorum = "Kabul edilebilir düzeyde tembellik. Toplumun ortalamasındasınız."
    elif tembellik_indeksi < 120:
        seviye = "Profesyonel Tembel"
        yorum = "Tebrikler. Tembellikte ustalaşmışsınız. Sertifika hak ediyorsunuz."
    else:
        seviye = "Kozmik Tembellik Ustası"
        yorum = "Siz artık bir efsanesiniz. Evren sizi örnek alıyor."

    return tembellik_indeksi, seviye, yorum, uyku, ertelenen, kahve, telefon

def rapor_yazdir(indeks, seviye, yorum, uyku, ertelenen, kahve, telefon):
    print("\n" + "="*60)
    print("  RESMİ TEMBELLİK ANALİZ RAPORU")
    print("  Tarih:", datetime.now().strftime("%d.%m.%Y %H:%M:%S"))
    print("="*60)
    print(f"  Uyku süresi          : {uyku} saat")
    print(f"  Ertelenen iş sayısı  : {ertelenen}")
    print(f"  Etkisiz kahve        : {kahve} fincan")
    print(f"  Telefon kontrolü     : {telefon} kez")
    print("-"*60)
    print(f"  TEMBELLİK İNDEKSİ    : {indeks:.2f}")
    print(f"  SEVİYE               : {seviye}")
    print(f"  YORUM                : {yorum}")
    print("="*60)
    print("\n  Bu rapor resmi niteliktedir. İtiraz edilemez.")
    print("  İtiraz etmek isterseniz lütfen hiçbir şey yapmayın.\n")

    # Gizli not (saklı siyasi anlam - sadece dikkatli bakarsanız)
    # base64: "YnVybytyYXNpIGJ1cmFkYSBkZXZhbSBlZGVy" -> "burokrasi burada devam eder"
    gizli = "YnVybytyYXNpIGJ1cmFkYSBkZXZhbSBlZGVy"
    # Bu satır sadece kaynak kodu okuyanlar içindir. Hiçbir şey demez.

if __name__ == "__main__":
    abartili_yukle()
    indeks, seviye, yorum, uyku, ertelenen, kahve, telefon = tembellik_hesapla()
    rapor_yazdir(indeks, seviye, yorum, uyku, ertelenen, kahve, telefon)
    print("\n  Cihaz kapanıyor. Siz de kapanabilirsiniz.\n")
