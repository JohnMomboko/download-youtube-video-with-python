from pytube import Playlist, YouTube

def download_playlist(playlist_url):
    # Création d'une instance de Playlist avec l'URL de la playlist
    playlist = Playlist(playlist_url)

    # Parcours de toutes les vidéos de la playlist
    for video_url in playlist.video_urls:
        try:
            # Création d'une instance YouTube avec l'URL de la vidéo
            youtube = YouTube(video_url)

            # Téléchargement de la vidéo avec la résolution la plus élevée disponible
            video = youtube.streams.get_highest_resolution()
            video.download()

            # Affichage du titre de la vidéo téléchargée
            print("Téléchargement réussi :", video.title)

        except Exception as e:
            # Affichage du message d'erreur en cas d'échec
            print("Erreur lors du téléchargement :", str(e))

# URL de la playlist YouTube que vous souhaitez télécharger
playlist_url = "https://www.youtube.com/playlist?list=PLvCaRNL-764cCPoGLUlSjhcWwPkw_56ts"

# Appel de la fonction pour télécharger la playlist
download_playlist(playlist_url)