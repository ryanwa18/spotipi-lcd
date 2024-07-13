import spotipy
from spotipy.oauth2 import SpotifyOAuth
import time
from bs4 import BeautifulSoup
import pyautogui

CLIENT_ID = "1a35d17e2a7747d8a4901cca2f5af892"
CLIENT_SECRET = "02cd43644d4e4e728b6bdc6834f86a5c"
REDIRECT_URI = "http://localhost/redirect"

scope = "user-read-currently-playing,user-modify-playback-state,user-read-playback-state"
auth_manager = SpotifyOAuth(CLIENT_ID, CLIENT_SECRET, REDIRECT_URI, scope=scope)
sp = spotipy.Spotify(auth_manager=auth_manager)
currSong = None
prevSong = None
deviceId = None

def display_song(song):
  if song == None:
    return

  with open("index.html") as fp:
    # Update web page with new song info
    soup = BeautifulSoup(fp, features="html.parser")
    soup.img["src"] = song["art"]
    soup.find("div", {"class": "bg-image"})["style"] = "background-image: url('" + song["art"] + "')" 
    soup.h1.string.replace_with(song["title"])
    soup.h2.string.replace_with(song["artist"])
    new_text = soup.prettify()
            
    with open("index.html", mode='w') as new_html_file:
        new_html_file.write(new_text)
  
  pyautogui.hotkey('command', 'r')

def change_state(state, device):
    # If either state or device is null exit
    if state == None or device == None:
        return
    
    try:
        if state == "play":
            sp.start_playback(device_id=device)
        elif state == "pause":
            sp.pause_playback(device_id=device)
        elif state == "next":
            sp.next_track(device_id=device)
        elif state == "previous":
            sp.previous_track(device_id=device)
        else:
            print("Unknown state")
    except Exception as e:
      print("Playback is already in current state: " + state)
    

def main():
    global currSong
    global prevSong
    global deviceId
    
    # Get current song and playback info from Spotify
    song = sp.current_user_playing_track()
    playback = sp.current_playback()

    # Check if playback info was returned
    if playback != None:
        deviceId = playback['device']['id']
    
    # Check if song info was returned
    if song != None:
        currSong = song["item"]["name"]
    
    # If song has changed
    if (currSong != prevSong):
        prevSong = currSong
        albumArt = song["item"]["album"]["images"][0]["url"]
        artist = song["item"]["artists"][0]["name"]
        display_song({"title": currSong, "art": albumArt, "artist": artist})
        print(currSong)


if __name__=="__main__":
    while(True):
        time.sleep(5)
        main() 
