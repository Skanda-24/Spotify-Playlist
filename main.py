import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
from dotenv import find_dotenv,load_dotenv

dotenv_path=find_dotenv()
load_dotenv(dotenv_path)

BILLBOARDS_URL=os.getenv("a")
CLIENT_ID=os.getenv("b")
CLIENT_SECREY=os.getenv("c")
USERNAME=os.getenv("d")
DOCUMENT_TXT=os.getenv("e")
PLAYLIST_ID=os.getenv("f")

day =input("Enter the date u want in form of:YYYY-MM-DD")
res=requests.get(f"{BILLBOARDS_URL}{day}/")
web=res.text
soup=BeautifulSoup(web,"html.parser")
data=soup.select("li ul li h3")
names=[]
for val in data:
    names.append(val.getText().strip())
client_ids=CLIENT_ID
client_secrey=CLIENT_SECREY
sp=spotipy.Spotify(
    auth_manager=SpotifyOAuth(
    client_id =client_ids,
    client_secret= client_secrey,
    redirect_uri= "https://example.com",
    scope ="playlist-modify-private",
    cache_path =DOCUMENT_TXT,
    username=USERNAME,
    show_dialog=True,
    )
)
user_id=sp.current_user()["id"]
year=day.split("-")[0]
uris=[]
for name in names:
    result=sp.search(q=f"track:{name} year:{year}",type="track")
    try:
        uri=result["tracks"]["items"][0]["uri"]
        uris.append(uri)
    except:
        print("Song not found")
newplay=sp.user_playlist_create(name="New playlist Python" , public=False,collaborative=False,description="",user=user_id)
playlist__id=PLAYLIST_ID
try:
    add_tracks=sp.playlist_add_items(playlist_id=newplay["id"] , items=uris)
except:
    print(f"Song not found")










