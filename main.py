import spotipy
from spotipy.oauth2 import SpotifyOAuth
import time

CLIENT_ID = "1a35d17e2a7747d8a4901cca2f5af892"
CLIENT_SECRET = "02cd43644d4e4e728b6bdc6834f86a5c"
REDIRECT_URI = "http://localhost/redirect"

scope = "user-read-currently-playing,user-modify-playback-state,user-read-playback-state"
auth_manager = SpotifyOAuth(CLIENT_ID, CLIENT_SECRET, REDIRECT_URI, scope=scope)
sp = spotipy.Spotify(auth_manager=auth_manager)

def main(): 
    print(sp.current_user_playing_track())
    playback = sp.current_playback()
    #device = playback['device']['id']
    #time.sleep(5)
    #sp.next_track(device_id=device)
    #time.sleep(5)
    #sp.previous_track(device_id=device)
    #time.sleep(5)
    #sp.volume(volume_percent=50,device_id=device)


if __name__=="__main__": 
    main() 
