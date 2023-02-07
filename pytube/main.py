from pytube import YouTube


yt = YouTube('https://www.youtube.com/watch?v=5PtUW4ULTTs')

for item in yt.streams:
    print(item)

stream = yt.streams.get_by_itag(313)
stream.download()