#!/bin/bash

# Hedef IP
TARGET_IP="192.168.1.107"

# IP adresi bilgisi gösterimi
echo "Hedef IP: $TARGET_IP"
echo "Tarama başlatılıyor..."

# 1. Hızlı port taraması
echo "[1] Temel port taraması..."
nmap $TARGET_IP -oN scan_basic.txt

# 2. Servis ve sürüm tespiti
echo "[2] Servis ve sürüm bilgisi taraması..."
nmap -sV $TARGET_IP -oN scan_services.txt

# 3. Zafiyet taraması
echo "[3] Zafiyet taraması..."
nmap -sV --script vuln $TARGET_IP -oN scan_vuln.txt

echo "Tüm taramalar tamamlandı."
echo "Çıktılar: scan_basic.txt, scan_services.txt, scan_vuln.txt"
