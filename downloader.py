from pytube import YouTube, Playlist
import ffmpeg
import os
import music_tag


def download_playlist(path, playlist_url, resolution, format='mp4'):
    try:
        #check if playlist or single video
        if any(x in playlist_url for x in ['list=', 'playlist']):
            p = Playlist(playlist_url)
            print(path)
            print('Number of videos in playlist: %s' % len(p.video_urls))
            for video in p.videos:
                #only audio
                if format == 'mp3':
                    video.streams.filter(only_audio=True).first().download(path)
                else:
                    if resolution == 'High Res':
                        #download video in highest resolution
                        video.streams.get_highest_resolution().download(path)
                    else:
                        #download video in lowest resolution
                        video.streams.get_lowest_resolution().download(path)
        else:
            #download single video
            yt = YouTube(playlist_url)
            if format == 'mp3':
                yt.streams.filter(only_audio=True).first().download(path)
            else:
                if resolution == 'High Res':
                    yt.streams.get_highest_resolution().download(path)
                else:
                    yt.streams.get_lowest_resolution().download(path)
        return True
    except:
        return False
    
def convert_mp3(path, quality='320k'):
    try:
        # convert every mp4 file to mp3
        for file in os.listdir(path):
            if file.endswith(".mp4"):
                file = os.path.join(path, file)
                filename = os.path.splitext(file)[0]
                if quality == '320k':
                    # convert to 320k mp3
                    ffmpeg.input(file).output(f"{filename}.mp3", acodec='libmp3lame', ac=2, ar='44100', ab='320k').run()
                else:
                    # convert to 128k mp3
                    ffmpeg.input(file).output(f"{filename}.mp3", acodec='libmp3lame', ac=2, ar='44100', ab='128k').run()
                os.remove(file)
        return True
    except:
        return False
            
def tag_mp3(path, artist, album, genre):
    #add tags to mp3 files
    try:
        for file in os.listdir(path):
            if file.endswith(".mp3"):
                # add artist and album tags
                file = os.path.join(path, file)
                tag = music_tag.load_file(file)
                tag['artist'] = artist
                tag['album'] = album
                tag['genre'] = genre
                tag.save()
        return True
    except:
        return False
