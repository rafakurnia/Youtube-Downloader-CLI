from yt_dlp import YoutubeDL
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
    ydl_opts = {
        'quiet': True,
        'skip_download': True,
    }

    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
    
    print("Judul: ", info.get("title"))
    print("Nama Chanel: ", info.get("uploader"))
    print("Views: ", info.get("view_count"))
    return info

def download_video(info):
    print("==================\n"
          "1. Resolusi Tinggi\n"
          "2. Resolusi Rendah\n")
    while True:
        opsi = input("Ingin Video Yang bagaimana? ")
        if opsi in ["1", "2"]:
            break

    if opsi == "1":
        format_code = "best"
    elif opsi == "2":
        format_code = "worst"

    print("="*40)
    print("Resolusi: ", format_code.upper())
    print("Tipe File: video/mp4 (default)")
    print("="*40)

    lanjut = input("Ingin mendownload (y/n)? ")
    if lanjut.lower() == "y":
        ydl_opts = {
            'format': format_code,
            'outtmpl': '%(title)s.%(ext)s'
        }
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([info.get("webpage_url")])
        print("✅ Download Berhasil!! 📺📺📺")
    else:
        print("⛔ DIBATALKAN!")
    print("="*40)

# Main flow
url = input_url()
video_info = buat_objek_video(url)
if video_info:
    download_video(video_info)
