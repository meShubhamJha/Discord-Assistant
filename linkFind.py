from spotify_client import SpotifyClient
spotify_client = SpotifyClient('BQCNCbfAnZ_2aMZSFLbLTNk2EOcJjvD48s2luY99qUeYPFAcuKAc4_JtJ9fUVHe4SW-qYX9cVInJB5CALgmc9lV7ZcD20gKeqyeL7n0vnyQ_kxvHP85I6Z-FANW1umICbrGHM6_Tt2OgZZdaoUjQmr4u287huaU')
def giveSong(song, artist=None):
    print(song, artist)
    spotify_song_id = spotify_client.search_song(song, artist)
    print(spotify_song_id)
    return "https://open.spotify.com/track/"+spotify_song_id
