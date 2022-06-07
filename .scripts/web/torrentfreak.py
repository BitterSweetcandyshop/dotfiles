import pywal
from subprocess import run
import requests
import os
# BitterSweet! why not properly parse through
#the html instead of spamming split() statments!!!
# REASON: why would I want to be effecient when I
#like eating spaghetti
try:
    tf_web = requests.get("https://torrentfreak.com/top-10-most-torrented-pirated-movies/").text
    tf = tf_web.split("</tr>\n</tfoot>\n<p><body></p>\n<tr>")[1].split("</tr>\n<p></body></table>\n<style>")[0].split("</tr>\n<tr>")

    top_ten = ""
    for i, torrent in enumerate(tf):
        item = {}
        torrent = torrent.splitlines()
        item["title"] = torrent[3][4:-5]
        item["title_fixed"] = torrent[3][4:-5]
        if len(item["title"]) > 10:
            item["title_fixed"] = item["title"][:7] + "..."
        item["rating"] = torrent[4].split("</a> / ")[0].split(">")[-1]
        item["imdb"] = torrent[4].split("<a href=\"")[1].split("\"")[0]

        # I could really put anything here since the ods a movie title uses <<&&>> or something is small
        top_ten += f"{item['rating']}bewbies{item['title']}bewbies{item['imdb']}bewbies{item['title_fixed']}\n"

    top_file = open(f"/home/{os.getlogin()}/.scripts/resources/tf_tops.txt", "w")
    top_file.write(top_ten[:-1])
    top_file.close()

    cover_url = "https://torrentfreak.com/images" + tf_web.split('<noscript><img src="https://torrentfreak.com/images')[1].split(" ")[0]
    cover = open(f"/home/{os.getlogin()}/.scripts/resources/tf_cover.png", "wb")
    cover_data = requests.get(cover_url)
    cover.write(cover_data.content)
    cover.close()
except:
    pass
#print(tf)




#https://i3.ytimg.com/vi/wxN1T1uxQ2g/maxresdefault.jpg
#https://www.youtube.com/watch?v=wxN1T1uxQ2g
#https://www.imdb.com/title/tt6710474/
#pyW = pywal.colors.get(f"/home/{os.getlogin()}/.scripts/resources/tf_cover.png")
#print(pyW["special"]["background"])
