from pytube import YouTube
import os

yt = YouTube(str(input("URL/Link of the video: >>")))
                       
video = yt.streams.filter(only_audio=True).first()

print("Enter the destination(Leave blank or current directory)")
destination = str(input(">>")) or '.'

outfile = video.download(output_path=destination)

base, ext = os.path.splitext(out_file)
new_file = base + '.mp3'
os.rename(out_file, new_file)

print(yt.title +"Has successfully been download in mp3 format.")