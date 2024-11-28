import tkinter as tk
from tkinter import messagebox

def calculate_bmi_metrics():
    try:
        weight = float(entry_weight.get())
        height = float(entry_height.get())
        bmi = weight / (height ** 2)
        display_bmi_result(bmi)
    except ValueError:
        messagebox.showerror("Gecersiz Girdi", "Lütfen agırlık ve boy icin gecerli sayılar girin.")

def calculate_bmi_imperial():
    try:
        weight = float(entry_weight.get())
        height = float(entry_height.get())
        weight_in_pounds = weight * 2.2
        height_in_inches = height / 0.0254
        bmi = (weight_in_pounds * 703) / (height_in_inches ** 2)
        display_bmi_result(bmi)
    except ValueError:
        messagebox.showerror("Gecersiz Girdi", "Lütfen agırlık ve boy icin gecerli sayılar girin.")

def display_bmi_result(bmi):
    if bmi <= 18.5:
        result = f"BMI: {bmi:.2f} - Zayıf. Daha düzenli ve yag acısından zengin beslenmelisiniz."
    elif 18.5 < bmi <= 24.9:
        result = f"BMI: {bmi:.2f} - Normal. Tebrikler, saglıklı bir kilodasınız!"
    elif 25 <= bmi <= 29.9:
        result = f"BMI: {bmi:.2f} - Fazla kilolu. Kilonuzu kontrol altında tutmaya calışın."
    else:
        result = f"BMI: {bmi:.2f} - Obezite. Saglık uzmanına danısmanız önerilir."
    messagebox.showinfo("BMI Sonucu", result)

# Tkinter GUI oluşturma
root = tk.Tk()
root.title("BMI Hesaplayıcı")

# Kullanıcı girdileri
frame = tk.Frame(root)
frame.pack(pady=10)

tk.Label(frame, text="Agırlık (kg):").grid(row=0, column=0, padx=5, pady=5)
entry_weight = tk.Entry(frame)
entry_weight.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame, text="Boy (m):").grid(row=1, column=0, padx=5, pady=5)
entry_height = tk.Entry(frame)
entry_height.grid(row=1, column=1, padx=5, pady=5)

# Hesaplama düğmeleri
frame_buttons = tk.Frame(root)
frame_buttons.pack(pady=10)

btn_metrics = tk.Button(frame_buttons, text="BMI (Metrik)", command=calculate_bmi_metrics)
btn_metrics.grid(row=0, column=0, padx=10)

btn_imperial = tk.Button(frame_buttons, text="BMI (İngiliz)", command=calculate_bmi_imperial)
btn_imperial.grid(row=0, column=1, padx=10)

# Çıkış düğmesi
btn_exit = tk.Button(root, text="Cıkıs", command=root.quit)
btn_exit.pack(pady=10)

# Uygulamayı çalıştırma
root.mainloop()
