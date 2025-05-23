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

## 🐧 Linux Sürümü: `port_scan.sh` (2. Cihaz da port taraması)

Linux (özellikle Kali) ortamında çalışan bu betik, hedef cihaz üzerinde otomatik Nmap taramaları gerçekleştirir.

### 📄 Yaptığı İşlemler:

- Hedef IP’yi tanımlar (`192.168.1.107` gibi)
- Temel port taraması yapar (`nmap`)
- Servis ve sürüm bilgisi toplar (`-sV`)
- Zafiyet taraması gerçekleştirir (`--script vuln`)
- Çıktıları ayrı `.txt` dosyalarına kaydeder:
  - `scan_basic.txt`
  - `scan_services.txt`
  - `scan_vuln.txt`

### ⚙️ Gereksinimler:

- Kali Linux (veya benzeri Linux)
- `nmap` aracı kurulu olmalı

### ▶️ Kullanım:

```bash
chmod +x port_scan.sh
./port_scan.sh
```

### 🎯 Amaç:

Bu betik, Linux ortamında manuel işlem gerektirmeden temel güvenlik kontrollerinin yapılmasını sağlar. Eğitim ve deneme/test amaçlıdır.

> Bu betik, ikinci cihazın analizi kapsamında geliştirilmiş olup [Pull Request #1](https://github.com/gismo-o/nmap-dokumani/pull/1) ile projeye dahil edilmiştir.
