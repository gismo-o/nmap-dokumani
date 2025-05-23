# 🔍 Nmap Tarama Komutları (.bat Otomasyonu)

Bu proje, temel ağ güvenliği testlerini otomatik olarak gerçekleştirmek için hazırlanmış bir `.bat` (Windows Batch) dosyasını içerir.

## 📌 İçerik

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

## 🛠 Kullanım

1. `nmap-tarama.bat` dosyasını çift tıklayarak çalıştırın
2. CMD ekranı açılır ve işlemler otomatik olarak yapılır
3. Sonuçlar ekranda görüntülenir

## 🎯 Amaç

Bu betik, bilgi güvenliği eğitimi ve temel zafiyet testleri içindir. Gerçek sistemlerde kullanılmadan önce mutlaka izin alınmalıdır.

## 📁 Not

Varsayılan IP adresi `192.168.1.13` olarak ayarlanmıştır. Kendi cihazınızın IP’sini `ipconfig` ile öğrenip `.bat` dosyasında düzenleyebilirsiniz.

---

### 👨‍⚖️ Yasal Uyarı

Bu araç sadece **yasal ve izinli testler** için kullanılmalıdır. İzinsiz ağ taramaları etik değildir ve yasal sorunlara yol açabilir.
