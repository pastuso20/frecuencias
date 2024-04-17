import subprocess

def abrir_video_en_edge(video_url):
    # Comando para ejecutar Microsoft Edge con la URL del video
    comando = f'start microsoft-edge:{video_url}'
    subprocess.Popen(comando, shell=True)

def main():
    video_url = "https://www.youtube.com/watch?v=TcMBFSGVi1c"
    abrir_video_en_edge(video_url)

if __name__ == "__main__":
    main()
