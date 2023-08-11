import requests
from bs4 import BeautifulSoup

output = open("output.txt", "a") #output.txt for outputs

spotifyURLtxt = open("./playlist.txt", "r", encoding="utf-8") #playlist.txt is for input. you should fill it correctly.
spotifyURLtxt = spotifyURLtxt.read() 
spotifyURLList = spotifyURLtxt.split("\n")
spotifyID = []

for ID in spotifyURLList:
    spotifyID.append(ID.split("/")[-1])

songLinkList = []
for ID in spotifyID:
    songLinkItem = f"https://song.link/s/{ID}"
    songLinkList.append(songLinkItem)

ytList = []
count = 0
for song_url in songLinkList:
    count += 1 # added for debubbing. you can use detect for songs have no yutub match.
    print(f"işlenen: {count}")
    htmlParse = ""
    response = requests.get(song_url)
    soup = BeautifulSoup(response.content, "html.parser")
    htmlParse = soup.find("a", href=lambda href: href and "https://www.youtube.com/watch" in href) # bs parsing the song.link page's source and finds the line has yutub. 
    htmlParse = str(htmlParse)
    try:
        htmlParse = htmlParse.split('"')[7]
        # eighth index is the yutub link.
    except IndexError:
        print(f"{count}: yutub link yok")
        # some song.link queries has no yutub match.
        continue
    output.write(f"{htmlParse}\n")