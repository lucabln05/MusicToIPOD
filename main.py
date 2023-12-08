from pytube import YouTube, Playlist
import ffmpeg
import os
import music_tag

playlist_url = input("Enter playlist url: ")
artist = input("Enter artist name: ")
album = input("Enter album name: ")
genre = input("Enter genre: ")

p = Playlist(playlist_url)

print('Number of videos in playlist: %s' % len(p.video_urls))
for video in p.videos:
    title = video.title
    print(f"{title}.mp4")
    #only audio
    video.streams.filter(only_audio=True).first().download()

# convert every mp4 file to mp3
for file in os.listdir():
    if file.endswith(".mp4"):
        filename = os.path.splitext(file)[0]
        print(filename)
        # mp3 is double the length of mp4 so fix that
        ffmpeg.input(file).output(f"{filename}.mp3", acodec='libmp3lame', ac=2, ar='44100', ab='192k').run()
        os.remove(file)
        

#add tags to mp3 files
for file in os.listdir():
    if file.endswith(".mp3"):
        # add artist and album tags
        tag = music_tag.load_file(file)
        tag['artist'] = artist
        tag['album'] = album
        tag['genre'] = genre
        tag.save()
