from tkinter import *
from tkinter import ttk
from fuzzy_logic import run_fuzzy_logic

class GreenhouseGUI:
    def __init__(self, master):
        self.master = master
        master.title("Akıllı Sera Kontrol Paneli")
        master.geometry("420x350")
        master.configure(bg="#f0f0f0")

        # Başlık
        title = Label(master, text="Girdi Değerlerini Giriniz", font=("Arial", 14, "bold"), bg="#f0f0f0")
        title.grid(row=0, column=0, columnspan=2, pady=10)

        # Girdi etiketleri ve kutuları
        self.entries = {}
        labels = ["Sıcaklık (°C)", "Hava Nemi (%)", "Toprak Nemi (%)", "Işık Şiddeti (lux)", "CO₂ Seviyesi (ppm)"]
        for idx, label in enumerate(labels):
            lbl = Label(master, text=label, font=("Arial", 11), bg="#f0f0f0")
            lbl.grid(row=idx+1, column=0, sticky=W, padx=20, pady=5)
            entry = Entry(master, width=20, font=("Arial", 11))
            entry.grid(row=idx+1, column=1, padx=10, pady=5)
            self.entries[label] = entry

        # Hesapla butonu
        calc_button = Button(master, text="Hesapla", command=self.calculate, bg="#4caf50", fg="white", font=("Arial", 11, "bold"))
        calc_button.grid(row=7, column=0, columnspan=2, pady=15)

        # Sonuç alanı
        self.result_label = Label(master, text="", font=("Arial", 12, "bold"), fg="blue", bg="#f0f0f0")
        self.result_label.grid(row=8, column=0, columnspan=2, pady=5)

    def calculate(self):
        try:
            inputs = [float(self.entries[label].get()) for label in self.entries]
            isitma, sulama = run_fuzzy_logic(*inputs)
            self.result_label.config(text=f"Isıtma: %{isitma:.2f}  |  Sulama: %{sulama:.2f}")
        except Exception as e:
            self.result_label.config(text=f"Hata: {e}", fg="red")
