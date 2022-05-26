from pytube import YouTube
url = input("Enter the Url of the youtube video to be downloaded: ")
my_video= YouTube(url)
print("*********************** Video Title *******************************")
print(my_video.title)
print("*********************** Download video **********************************")
my_video = my_video.streams.get_highest_resolution()
my_video.download
print("Download Successfull")
