import tkinter as tk
from tkinter import simpledialog
import logging
from datetime import datetime
import os

# --- LOGLAMA KURULUMU ---
# Log dosyasının adını ve konumunu belirleme
LOG_DIR = os.path.join(os.path.expanduser("~"), ".local", "share", "super_popup_app") # Kullanıcı ana dizininde gizli bir klasör
LOG_FILE = os.path.join(LOG_DIR, "app_log.txt")
	
# Log dizininin varlığını kontrol etme ve yoksa oluşturma
os.makedirs(LOG_DIR, exist_ok=True)

# Loglama ayarları
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO, # INFO seviyesindeki ve üstündeki olayları kaydet
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

# Uygulama başlangıcını kaydet
logging.info("--- Uygulama Başlatıldı ---")
# -------------------------


# Ana pencere
root = tk.Tk()
root.title("🌟 Süper Modern Popup Uygulaması")
root.geometry("500x250")
root.configure(bg="#1e1e2f")

# Başlık
baslik = tk.Label(root, text="Popup Uygulaması", font=("Helvetica", 20, "bold"), fg="#f1c40f", bg="#1e1e2f")
baslik.pack(pady=20)

# Buton çerçevesi
frame = tk.Frame(root, bg="#1e1e2f")
frame.pack(pady=20)


# Hover animasyonu fonksiyonları
def on_enter(e, btn, color):
    btn.config(bg=color)
    btn.config(font=("Helvetica", 14, "bold"))

def on_leave(e, btn, color):
    btn.config(bg=color)
    btn.config(font=("Helvetica", 13))

# Uygulama kapatıldığında log kaydı ekleme
def on_close():
    logging.info("--- Uygulama Kapatıldı ---")
    root.destroy()

# Çıkış butonu
cikis_butonu = tk.Button(frame, text="Çıkış", command=on_close, bg="#e74c3c", fg="white", font=("Helvetica", 13),
                         width=14, relief="flat")
cikis_butonu.pack(side="left", padx=25)
cikis_butonu.bind("<Enter>", lambda e: on_enter(e, cikis_butonu, "#c0392b"))
cikis_butonu.bind("<Leave>", lambda e: on_leave(e, cikis_butonu, "#e74c3c"))


# Modern popup fonksiyonu
def modern_popup():
    logging.info("Popup Butonuna tıklandı.")
    try:
        isim = simpledialog.askstring("İsim Girin", "Lütfen adınızı girin:")
        
        if isim is None: # Kullanıcı iptal etti
             logging.info("İsim girişi kullanıcı tarafından iptal edildi.")
             return
             
        if isim:
            logging.info(f"Girilen isim: {isim}")
            popup = tk.Toplevel()
            popup.title("🎉 Selam!")
            popup.geometry("300x150")
            popup.configure(bg="#34495e")
            popup.resizable(False, False)

            mesaj = tk.Label(popup, text=f"Merhaba, {isim}! 👋", font=("Helvetica", 14, "bold"), fg="#f1c40f", bg="#34495e")
            mesaj.pack(pady=30)
            
            # Popup kapatma fonksiyonu
            def popup_kapat():
                logging.info(f"'{isim}' için açılan popup kapatıldı.")
                popup.destroy()

            kapat_butonu = tk.Button(popup, text="Kapat", command=popup_kapat, bg="#e67e22", fg="white",
                                     font=("Helvetica", 12, "bold"), width=10, relief="flat")
            kapat_butonu.pack(pady=10)

            # Hover efektleri popup butonu için
            kapat_butonu.bind("<Enter>", lambda e: kapat_butonu.config(bg="#d35400"))
            kapat_butonu.bind("<Leave>", lambda e: kapat_butonu.config(bg="#e67e22"))
            
            # Popup'ın kapatma (X) düğmesi için de loglama
            popup.protocol("WM_DELETE_WINDOW", popup_kapat)
        else:
            logging.warning("Kullanıcı isim girmeden onayladı (boş isim).")
            popup = tk.Toplevel()
            popup.title("🎉 Selam!")
            popup.geometry("300x150")
            popup.configure(bg="#34495e")
            popup.resizable(False, False)

            mesaj = tk.Label(popup, text="Merhaba! Hoş geldiniz! 👋", font=("Helvetica", 14, "bold"), fg="#f1c40f",
                             bg="#34495e")
            mesaj.pack(pady=30)
            
            # Popup kapatma fonksiyonu
            def popup_kapat_hosgeldiniz():
                logging.info("Boş isim için açılan 'Hoş geldiniz' popup kapatıldı.")
                popup.destroy()

            kapat_butonu = tk.Button(popup, text="Kapat", command=popup_kapat_hosgeldiniz, bg="#e67e22", fg="white",
                                     font=("Helvetica", 12, "bold"), width=10, relief="flat")
            kapat_butonu.pack(pady=10)

            kapat_butonu.bind("<Enter>", lambda e: kapat_butonu.config(bg="#d35400"))
            kapat_butonu.bind("<Leave>", lambda e: kapat_butonu.config(bg="#e67e22"))
            
            popup.protocol("WM_DELETE_WINDOW", popup_kapat_hosgeldiniz)
            
    except Exception as e:
        logging.error(f"Popup oluşturulurken bir hata oluştu: {e}")
        
# Selamla butonu
popup_butonu = tk.Button(frame, text="Selamla", command=modern_popup, bg="#3498db", fg="white", font=("Helvetica", 13),
                         width=14, relief="flat")
popup_butonu.pack(side="right", padx=25)
popup_butonu.bind("<Enter>", lambda e: on_enter(e, popup_butonu, "#2980b9"))
popup_butonu.bind("<Leave>", lambda e: on_leave(e, popup_butonu, "#3498db"))

# Ana pencerenin kapatma (X) düğmesi için de loglama
root.protocol("WM_DELETE_WINDOW", on_close)

try:
    root.mainloop()
except Exception as e:
    logging.critical(f"Uygulama beklenmedik bir hata ile çöktü: {e}", exc_info=True)
    print(f"Kritik Hata: {e}")
