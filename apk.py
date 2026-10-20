import tkinter as tk

def prediksi():
    label_hasil.config(text="Prodi Pilihan: Teknologi Informasi")

root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan")

tk.Label(root, text="Aplikasi Prediksi Prodi Pilihan", font=("Arial", 12, "bold")).pack(pady=10)

for i in range(1, 11):
    frame = tk.Frame(root)
    frame.pack(anchor="w", padx=20, pady=2)
    tk.Label(frame, text=f"Nilai Mata Pelajaran {i} : ").pack(side="left")
    tk.Entry(frame).pack(side="left")

tk.Button(root, text="Hasil Prediksi", command=prediksi).pack(pady=10)

