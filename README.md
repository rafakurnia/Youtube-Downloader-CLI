<h1 align="center">🎬 YouTube Video Downloader</h1>
<p align="center">Python CLI app for downloading YouTube videos using <code>pytube</code> or <code>yt-dlp</code></p>

---

## 📌 Deskripsi

Proyek ini merupakan skrip Python CLI sederhana untuk mengunduh video dari YouTube. Tersedia dalam dua versi:

- 🔹 `pytube` — versi default
- 🔸 `yt-dlp` — versi alternatif jika `pytube` tidak dapat digunakan

---

## 🧩 Fitur

- Menampilkan **judul video**, **nama channel**, dan **jumlah views**
- Pilihan resolusi: **Tinggi** atau **Rendah**
- Konfirmasi download
- Antarmuka interaktif berbasis terminal

---

## 📁 Struktur File

| Nama File               | Keterangan                                        |
|------------------------|---------------------------------------------------|
| `downloader_pytube.py` | Downloader berbasis `pytube`                      |
| `downloader_ytdlp.py`  | Versi alternatif dengan `yt-dlp`                  |

---

## ⚙️ Instalasi

Pasang dependensi dengan `pip`:

```bash
# Versi utama
pip install pytube

# Versi alternatif
pip install yt-dlp
