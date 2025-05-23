@echo off
echo IP adresi bilgisi aliniyor...
ipconfig

echo.
echo === Nmap Port Taramasi Baslatiliyor ===
nmap 192.168.1.13

echo.
echo === Versiyon ve Servis Tespiti ===
nmap -sV 192.168.1.13

echo.
echo === SMB Zafiyet Taramasi ===
nmap -p445 --script smb-vuln* 192.168.1.13

echo.
echo === SMB Protokol Surum Tespiti ===
nmap -p445 --script smb-protocols 192.168.1.13

echo.
echo === SMB Kullanici Bilgisi Sızdırma Testi ===
nmap --script smb-enum-users -p445 192.168.1.13

echo.
echo === MySQL Zafiyet Taramasi ===
nmap -p3306 --script mysql* 192.168.1.13

echo.
echo === MySQL Kimlik Dogrulama Kontrolu ===
nmap -sV -p 3306 192.168.1.13

echo.
echo === Tum Islemler Tamamlandi ===
pause
