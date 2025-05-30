import tkinter as tk
from tkinter import messagebox, scrolledtext
import subprocess

# Komut çalıştırma fonksiyonu
def run_nmap(command, output_box):
    try:
        result = subprocess.check_output(command, shell=True, text=True)
        output_box.delete(1.0, tk.END)
        output_box.insert(tk.END, result)
    except subprocess.CalledProcessError as e:
        output_box.delete(1.0, tk.END)
        output_box.insert(tk.END, f"Hata: {e}")

# Arayüz fonksiyonu
def create_gui():
    window = tk.Tk()
    window.title("Nmap Tarama Arayüzü")
    window.geometry("800x540")

    tk.Label(window, text="Hedef IP Adresi:").pack(pady=5)
    ip_entry = tk.Entry(window, width=40)
    ip_entry.pack(pady=5)

    output_box = scrolledtext.ScrolledText(window, width=100, height=22)
    output_box.pack(pady=10)

    def run_scan(option):
        ip = ip_entry.get().strip()
        if not ip:
            messagebox.showwarning("Uyarı", "Lütfen bir IP adresi girin.")
            return

        if option == "basic":
            run_nmap(f"nmap {ip}", output_box)
        elif option == "version":
            run_nmap(f"nmap -sV {ip}", output_box)
        elif option == "smb":
            run_nmap(f"nmap -p445 --script smb-vuln* {ip}", output_box)
        elif option == "mysql":
            run_nmap(f"nmap -p3306 --script mysql* {ip}", output_box)
        elif option == "vmware-auth":
            run_nmap(f"nmap -p902 -sV {ip}", output_box)
        elif option == "apex-mesh":
            run_nmap(f"nmap -p912 -sV {ip}", output_box)
        elif option == "custom":
            port = custom_port_entry.get().strip()
            if not port.isdigit():
                messagebox.showwarning("Uyarı", "Geçerli bir port numarası girin.")
                return
            run_nmap(f"nmap -p{port} -sV {ip}", output_box)

    btn_frame = tk.Frame(window)
    btn_frame.pack(pady=10)

    # Butonlar
    tk.Button(btn_frame, text="Temel Port Taraması", command=lambda: run_scan("basic"), width=22).grid(row=0, column=0, padx=5, pady=5)
    tk.Button(btn_frame, text="Servis/Versiyon Bilgisi", command=lambda: run_scan("version"), width=22).grid(row=0, column=1, padx=5, pady=5)
    tk.Button(btn_frame, text="SMB Zafiyet Taraması", command=lambda: run_scan("smb"), width=22).grid(row=1, column=0, padx=5, pady=5)
    tk.Button(btn_frame, text="MySQL Zafiyet Taraması", command=lambda: run_scan("mysql"), width=22).grid(row=1, column=1, padx=5, pady=5)
    tk.Button(btn_frame, text="VMware Auth (902) Taraması", command=lambda: run_scan("vmware-auth"), width=22).grid(row=2, column=0, padx=5, pady=5)
    tk.Button(btn_frame, text="Apex Mesh (912) Taraması", command=lambda: run_scan("apex-mesh"), width=22).grid(row=2, column=1, padx=5, pady=5)

    # Özel port tarama alanı
    custom_frame = tk.Frame(window)
    custom_frame.pack(pady=5)
    tk.Label(custom_frame, text="Manuel Port:").pack(side=tk.LEFT, padx=3)
    custom_port_entry = tk.Entry(custom_frame, width=8)
    custom_port_entry.pack(side=tk.LEFT, padx=3)
    tk.Button(custom_frame, text="Özel Port Taraması", command=lambda: run_scan("custom"), width=18).pack(side=tk.LEFT, padx=3)

    window.mainloop()

# Programı başlat
create_gui()
