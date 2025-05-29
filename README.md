# 🔍 Nmap Tarama Komutları (.bat Otomasyonu)

Bu proje, temel ağ güvenliği testlerini otomatik olarak gerçekleştirmek için hazırlanmış bir `.bat` (Windows Batch) dosyasını içerir.

## İçerik

`.bat` dosyası şu işlemleri sırasıyla yapar:

- IP adresi tespiti (`ipconfig`)
- Temel port taraması (`nmap`)
- Servis ve versiyon bilgisi alma
- SMB servislerine yönelik zafiyet taramaları (MS10-054, MS10-061)
- SMB protokol sürümü kontrolü (SMBv1, SMBv2, SMBv3)
- SMB kullanıcı bilgisi sızdırma testi
- MySQL portu üzerindeki zafiyet ve brute-force testleri

## ⚠️ Gereksinimler

- Windows işletim sistemi
- [Nmap](https://nmap.org/download.html) yüklü olmalıdır
  - Nmap yüklü değilse `.bat` dosyası çalışmaz

##  Kullanım

1. `nmap-tarama.bat` dosyasını çift tıklayarak çalıştırın
2. CMD ekranı açılır ve işlemler otomatik olarak yapılır
3. Sonuçlar ekranda görüntülenir

##  Amaç

Bu betik, bilgi güvenliği eğitimi ve temel zafiyet testleri içindir. 

## Not

Varsayılan IP adresi `192.168.1.13` olarak ayarlanmıştır. Kendi cihazınızın IP’sini `ipconfig` ile öğrenip `.bat` dosyasında düzenleyebilirsiniz.

---

# Nmap Port Tarama GUI

Bu proje, **Nmap** kullanarak ağ ve sistemler üzerinde port taraması yapmayı sağlayan Python tabanlı basit bir grafik arayüz uygulamasıdır.  
Program, farklı tarama seçenekleriyle ağ üzerindeki cihazların açık portlarını kolayca tespit etmenizi sağlar.

## Özellikler

- Hedef IP adresine göre temel port taraması
- Servis ve sürüm bilgisi taraması
- SMB ve MySQL zafiyet taramaları
- VMware Auth (902) ve Apex Mesh (912) gibi özel portlar için hızlı tarama
- Dilediğin portu manuel olarak tarayabilme (özel port kutusu)

## Kullanım

1. **Gereksinimler:**
   - Python 3
   - Tkinter (`sudo apt install python3-tk`)
   - Nmap (`sudo apt install nmap`)

2. **Çalıştırmak için:**
   ```sh
   python3 port_tarama_gui.py

