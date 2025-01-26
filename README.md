# YTDWL
Basitleştirilmiş Türkçe Youtube Video ve Ses indirme Aracı
# YouTube Video İndirici

**YTDWL**, YouTube videolarını indirmenizi sağlayan basit bir Python programıdır. Bu program, video veya sadece ses dosyalarını indirmenize olanak tanır. Program, kullanıcıya video URL'sini, çözünürlük seçeneklerini ve ses indirip indirmeme tercihini sorar, ardından dosyayı belirtilen dizine indirir.

## Kurulum

Bu programı çalıştırabilmek için `yt-dlp` kütüphanesinin yüklü olması gerekmektedir.

1. Python 3 ve `pip` kurulu olduğundan emin olun.
2. `yt-dlp` kütüphanesini yüklemek için terminale şu komutu yazın:

```bash
sudo pip install yt-dlp
```
**İndirme**
```bash
git clone https://github.com/Alonera/YTDWL.git
```
**KULLANIM**
  1. Programı çalıştırın:
  ```bash
python3 YTDWL.py
  ```
  3. İndirmek istediğiniz YouTube video URL'sini girin.
  4. Çözünürlük seçeneğini (1080p, 720p, 480p, 360p) belirleyin.
  5. Sadece ses mi indirmek istediğinizi belirtin.
  6. Kaydedilecek dizini seçin (Varsayılan: /home/{kullanıcı_adı}/YTDWL).
  7. Program video veya ses dosyasını indirip belirtilen dizine kaydedecektir.
