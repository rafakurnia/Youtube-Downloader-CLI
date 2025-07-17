from pytube import YouTube
import time

print("="*50)

def input_url():
    print("="*10, " SELAMAT DATANG DI YOUTUBE DOWNLOADER ", "="*10)
    while True:
        url = str(input("url = ").strip())
        if "youtube.com/watch?v=" in url or "youtu.be/" in url:
            print("-"*5, " Valid ", "-"*5)
            break
        else:
            print("-"*50)
            print("Masukan url yang benar: ")

    print("Mencari video....")
    time.sleep(2)
    return url 

def buat_objek_video(url):
    try:
        video = YouTube(url)
        print("Judul: ", video.title)
        print("Nama Chanel: ", video.author)
        print("Views: ", video.views)
        return video
    except Exception as e:
        print("Gagal Memuat! Coba lagi.")
        print("Error:", e)
        return None

def download_video(video):
    print("==================\n"
          "1. Resolusi Tinggi\n"
          "2. Resolusi Rendah\n")
    while True:
        opsi = input("Ingin Video Yang bagaimana? ")
        if opsi in ["1", "2"]:
            break

    if opsi == "1":
        stream = video.streams.get_highest_resolution()
    elif opsi == "2":
        stream = video.streams.get_lowest_resolution()

    print("="*40)
    print("Resolusi: ", stream.resolution)
    print("Tipe File:", stream.mime_type)
    print("="*40)

    lanjut = input("Ingin mendownload (y/n)? ")
    if lanjut.lower() == "y":
        stream.download()
        print("✅ Download Berhasil!! 📺📺📺")
    else:
        print("⛔ DIBATALKAN!")
    print("="*40)

# Main flow
url = input_url()
video = buat_objek_video(url)
if video:
    download_video(video)
