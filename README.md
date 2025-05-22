# Fuzzy-Logic-Based-Smart-Greenhouse-Controller

# Akıllı Sera İklim Kontrol Sistemi

Bu proje, Python kullanılarak geliştirilen ve bulanık mantık tabanlı bir sera iklim kontrol sistemidir. Sistem, 5 farklı çevresel girdi alarak (sıcaklık, hava nemi, toprak nemi, ışık şiddeti, CO₂ seviyesi) iki çıktı üretir: ısıtma/soğutma ve sulama/ventilasyon gücü.

## Özellikler

- Kullanıcı dostu arayüz (Tkinter ile)
- scikit-fuzzy kullanılarak bulanık mantık kontrolü
- Gerçek zamanlı simülasyon

## Gerekli Kütüphaneler

```
numpy
scikit-fuzzy
matplotlib

```

## Kullanım

```
python main.py
```

## Girişler ve Çıkışlar

| Girdi            | Açıklama             |
|------------------|----------------------|
| Sıcaklık         | 0 - 50 °C            |
| Hava Nemi        | 0 - 100 %            |
| Toprak Nemi      | 0 - 100 %            |
| Işık Şiddeti     | 0 - 10000 lux        |
| CO₂ Seviyesi     | 300 - 1500 ppm       |

| Çıktı            | Açıklama             |
|------------------|----------------------|
| Isıtma Gücü      | 0 - 100 %            |
| Sulama Gücü      | 0 - 100 %            |
