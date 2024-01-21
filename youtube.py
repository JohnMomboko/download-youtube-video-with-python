from pytube import YouTube

def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage = (bytes_downloaded / total_size) * 100
    print(f"Téléchargement en cours : {percentage:.2f}%")

def download_video(video_url):
    try:
        # Création d'une instance YouTube avec l'URL de la vidéo
        youtube = YouTube(video_url)

        # Ajout du gestionnaire de progression
        youtube.register_on_progress_callback(on_progress)

        # Téléchargement de la vidéo avec la résolution la plus élevée disponible
        video = youtube.streams.get_highest_resolution()
        video.download()

        # Affichage du titre de la vidéo téléchargée
        print("Téléchargement réussi :", video.title)

    except Exception as e:
        # Affichage du message d'erreur en cas d'échec
        print("Erreur lors du téléchargement :", str(e))

# URL de la vidéo YouTube que vous souhaitez télécharger
video_url = "https://www.youtube.com/watch?v=L7xjjtVuIl4"

# Appel de la fonction pour télécharger la vidéo
download_video(video_url)