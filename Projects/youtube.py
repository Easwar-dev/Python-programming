import yt_dlp

def download_video(url, save_path):
    ydl_opts = {
        'outtmpl': f'{save_path}/%(title)s.%(ext)s',
        # 'best' tells it to get the best single file (video + audio together).
        # This usually maxes out at 720p but does NOT require FFmpeg.
        'format': 'best'
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("Video downloaded successfully!")
    except Exception as e:
        print(e)

url = "https://youtube.com/shorts/enpMZosdcAU?si=ZcOTFQ7dqUKlRoKK"
# Make sure your path uses forward slashes '/' or double backslashes '\\'
save_path = "E:/C programs"

download_video(url, save_path)