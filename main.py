import spotipy
from spotipy.oauth2 import SpotifyOAuth
import time

CLIENT_ID = "1a35d17e2a7747d8a4901cca2f5af892"
CLIENT_SECRET = "02cd43644d4e4e728b6bdc6834f86a5c"
REDIRECT_URI = "http://localhost/redirect"

scope = "user-read-currently-playing,user-modify-playback-state,user-read-playback-state"
auth_manager = SpotifyOAuth(CLIENT_ID, CLIENT_SECRET, REDIRECT_URI, scope=scope)
sp = spotipy.Spotify(auth_manager=auth_manager)
currSong = None
prevSong = None
deviceId = None

def change_state(state, device):
    # If either state or device is null exit
    if state == None or device == None:
        return

    if state == "play":
        sp.start_playback(device_id=device)
        print("Play")
    elif state == "pause":
        sp.pause_playback(device_id=device)
        print("Pause")
    elif state == "next":
        sp.next_track(device_id=device)
        print("Next")
    elif state == "previous":
        sp.previous_track(device_id=device)
        print("Previous")
    else:
        print("Unknown state")

def main():
    global currSong
    global prevSong
    global deviceId
    
    song = sp.current_user_playing_track()
    playback = sp.current_playback()

    # Check if playback info was returned
    if playback != None:
        deviceId = playback['device']['id']
        change_state("play", deviceId)
        time.sleep(2)
        change_state("pause", deviceId)
        time.sleep(2)
        change_state("next", deviceId)
        time.sleep(2)
        change_state("previous", deviceId)
        time.sleep(2)
    
    # Check if song info was returned
    if song != None:
        currSong = song["item"]["name"]
    
    # If song has changed
    if (currSong != prevSong):
        prevSong = currSong
        albumArt = song["item"]["album"]["images"][0]["url"]
        print(currSong)
        print(albumArt)

    #device = playback['device']['id']
    #time.sleep(5)
    #sp.next_track(device_id=device)
    #time.sleep(5)
    #sp.previous_track(device_id=device)
    #time.sleep(5)
    #sp.volume(volume_percent=50,device_id=device)


if __name__=="__main__":
    while(True):
        time.sleep(5)
        main() 
