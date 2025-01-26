#!/usr/bin/env python3
import os
import subprocess
import sys
import getpass
import time
import signal  # Bu satır eklendi

# Kütüphane kontrol fonksiyonu
def check_and_install_libraries():
    try:
        import yt_dlp
    except ImportError:
        print("yt-dlp kütüphanesi yüklü değil. Yüklemek için 'sudo pip install yt-dlp' komutunu kullanın.")
        sys.exit(1)

# Programı düzgün kapatmak için sinyal işlemi
def signal_handler(sig, frame):
    print("\nProgramdan çıkılıyor...")
    exit(0)

# Varsayılan indirme konumunu oluşturma
def create_default_directory():
    user_name = getpass.getuser()  # Kullanıcı adını al
    download_path = f"/home/{user_name}/YTDWL"
    
    # Klasör yoksa oluştur
    if not os.path.exists(download_path):
        os.makedirs(download_path)
        print(f"Varsayılan indirme klasörü oluşturuldu: {download_path}")
    return download_path

# Kullanıcı video indirme işlemi
def download_video(url, resolution='1080p', only_audio=False, save_path='.'):
    try:
        # yt-dlp komutunu hazırla
        command = ['yt-dlp', url]

        # Eğer yalnızca ses istiyorsa
        if only_audio:
            command.extend([
                '--extract-audio',
                '--audio-format', 'mp3',  # Ses formatını belirt
                '--audio-quality', '0',  # En iyi kalite
                '-o', os.path.join(save_path, '%(title)s.%(ext)s')
            ])
        else:
            # Video ve ses akışlarını seç
            command.extend([
                '-f', f'bestvideo[height<={resolution}]+bestaudio/best',  # Video ve sesi birleştir
                '--merge-output-format', 'mp4',  # Birleştirilmiş çıktıyı MP4 formatında sakla
                '-o', os.path.join(save_path, '%(title)s.%(ext)s')
            ])

        # Komutu yazdır ve çalıştır
        print(f"İndirme başlıyor... {url}")
        print("İndirme devam ediyor", end="")
        
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        # İndirme devam ettikçe noktalar ekle
        while process.poll() is None:
            print(".", end="", flush=True)
            time.sleep(1)

        # İndirme tamamlandığında
        print("\nİndirme ve birleştirme işlemi başarıyla tamamlandı!")

    except Exception as e:
        print(f"Hata oluştu: {e}")

# Kullanıcıdan video bilgilerini al
def user_input():
    while True:
        print("\nYouTube Video İndirici\n")
        url = input("İndirmek istediğiniz YouTube video linkini girin: ")

        print("\nÇözünürlük Seçenekleri: ")
        print("1. 1080p")
        print("2. 720p")
        print("3. 480p")
        print("4. 360p")
        resolution_choice = input("Çözünürlük seçin (1/2/3/4): ")

        resolution = '1080p' if resolution_choice == '1' else '720p' if resolution_choice == '2' else '480p' if resolution_choice == '3' else '360p'

        audio_only = input("\nSadece ses mi indirmek istersiniz? (y/n): ").strip().lower() == 'y'

        # Kaydetme yolunu sor
        save_path = input(f"Kaydedilecek dizin yolunu girin (Varsayılan: /home/{getpass.getuser()}/YTDWL): ").strip()

        # Kullanıcı bir yol girmezse varsayılanı kullan
        if not save_path:
            save_path = create_default_directory()

        print(f"\nSeçilen Ayarlar:\nÇözünürlük: {resolution}\nSadece Ses: {audio_only}\nKaydetme Yolu: {save_path}")
        download_video(url, resolution=resolution, only_audio=audio_only, save_path=save_path)

        # Ana menüye geri dönme
        continue_input = input("\nYeni bir video indirmek ister misiniz? (y/n): ").strip().lower()
        if continue_input != 'y':
            print("Çıkılıyor...")
            break

# Ana program
if __name__ == "__main__":
    # Kütüphanelerin yüklü olduğundan emin ol
    check_and_install_libraries()
    
    # Ctrl+C ile düzgün kapanmayı sağla
    signal.signal(signal.SIGINT, signal_handler)
    
    # Program çalışmaya başlasın
    user_input()

