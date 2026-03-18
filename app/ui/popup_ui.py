import logging
import tkinter as tk
from tkinter import simpledialog


class PopupApp:
    def __init__(self, logger: logging.Logger) -> None:
        self.logger = logger
        self.root = tk.Tk()
        self.root.title("Super Modern Popup Uygulamasi")
        self.root.geometry("500x250")
        self.root.configure(bg="#1e1e2f")
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

        self._build_ui()

    def _build_ui(self) -> None:
        baslik = tk.Label(
            self.root,
            text="Popup Uygulamasi",
            font=("Helvetica", 20, "bold"),
            fg="#f1c40f",
            bg="#1e1e2f",
        )
        baslik.pack(pady=20)

        frame = tk.Frame(self.root, bg="#1e1e2f")
        frame.pack(pady=20)

        cikis_butonu = tk.Button(
            frame,
            text="Cikis",
            command=self.on_close,
            bg="#e74c3c",
            fg="white",
            font=("Helvetica", 13),
            width=14,
            relief="flat",
        )
        cikis_butonu.pack(side="left", padx=25)
        cikis_butonu.bind("<Enter>", lambda e: self._on_enter(cikis_butonu, "#c0392b"))
        cikis_butonu.bind("<Leave>", lambda e: self._on_leave(cikis_butonu, "#e74c3c"))

        popup_butonu = tk.Button(
            frame,
            text="Selamla",
            command=self.modern_popup,
            bg="#3498db",
            fg="white",
            font=("Helvetica", 13),
            width=14,
            relief="flat",
        )
        popup_butonu.pack(side="right", padx=25)
        popup_butonu.bind("<Enter>", lambda e: self._on_enter(popup_butonu, "#2980b9"))
        popup_butonu.bind("<Leave>", lambda e: self._on_leave(popup_butonu, "#3498db"))

    def _on_enter(self, button: tk.Button, color: str) -> None:
        button.config(bg=color, font=("Helvetica", 14, "bold"))

    def _on_leave(self, button: tk.Button, color: str) -> None:
        button.config(bg=color, font=("Helvetica", 13))

    def on_close(self) -> None:
        self.logger.info("--- Uygulama Kapatildi ---")
        self.root.destroy()

    def _open_popup(self, message: str, close_log: str) -> None:
        popup = tk.Toplevel(self.root)
        popup.title("Selam")
        popup.geometry("300x150")
        popup.configure(bg="#34495e")
        popup.resizable(False, False)

        mesaj = tk.Label(
            popup,
            text=message,
            font=("Helvetica", 14, "bold"),
            fg="#f1c40f",
            bg="#34495e",
        )
        mesaj.pack(pady=30)

        def popup_kapat() -> None:
            self.logger.info(close_log)
            popup.destroy()

        kapat_butonu = tk.Button(
            popup,
            text="Kapat",
            command=popup_kapat,
            bg="#e67e22",
            fg="white",
            font=("Helvetica", 12, "bold"),
            width=10,
            relief="flat",
        )
        kapat_butonu.pack(pady=10)
        kapat_butonu.bind("<Enter>", lambda e: kapat_butonu.config(bg="#d35400"))
        kapat_butonu.bind("<Leave>", lambda e: kapat_butonu.config(bg="#e67e22"))
        popup.protocol("WM_DELETE_WINDOW", popup_kapat)

    def modern_popup(self) -> None:
        self.logger.info("Popup butonuna tiklandi.")
        try:
            isim = simpledialog.askstring("Isim Girin", "Lutfen adinizi girin:")
            if isim is None:
                self.logger.info("Isim girisi kullanici tarafindan iptal edildi.")
                return

            temiz_isim = isim.strip()
            if temiz_isim:
                self.logger.info("Girilen isim: %s", temiz_isim)
                self._open_popup(
                    message=f"Merhaba, {temiz_isim}!",
                    close_log=f"'{temiz_isim}' icin acilan popup kapatildi.",
                )
                return

            self.logger.warning("Kullanici bos isim ile onayladi.")
            self._open_popup(
                message="Merhaba! Hos geldiniz!",
                close_log="Bos isim popup penceresi kapatildi.",
            )
        except Exception as exc:
            self.logger.error("Popup olusturulurken hata olustu: %s", exc)

    def run(self) -> None:
        try:
            self.root.mainloop()
        except Exception as exc:
            self.logger.critical("Uygulama beklenmedik bir hata ile coktu: %s", exc, exc_info=True)
            print(f"Kritik Hata: {exc}")
