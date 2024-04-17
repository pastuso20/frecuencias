import speech_recognition as sr
import os

carpeta_abierta = False

def reconocer_voz():
    recognizer = sr.Recognizer()

    while True:
        with sr.Microphone() as source:
            print("Di algo...")
            audio = recognizer.listen(source)

            try:
                texto = recognizer.recognize_google(audio, language='es-ES')
                print("Texto reconocido:", texto)
                return texto.lower()  # Convertir texto a minúsculas para facilitar la comparación
            except sr.UnknownValueError:
                print("No se pudo entender el audio")
            except sr.RequestError as e:
                print("Error en la solicitud:", e)

def buscar_palabra_canguro(texto):
    global carpeta_abierta

    if "canguro" in texto:
        print("¡Se detectó la palabra 'canguro'!")
        if not carpeta_abierta:
            # Abre la carpeta
            os.system("start C:\\Users\\hp\\OneDrive\\Imágenes\\Mateo")
            carpeta_abierta = True
            print("¡Se abrió la carpeta!")
        else:
            # Cierra la carpeta
            os.system("taskkill /f /im explorer.exe")  # Cierra el Explorador de archivos en Windows
            carpeta_abierta = False
            print("¡Se cerró la carpeta!")
        return True  # La búsqueda de la palabra 'canguro' se ha completado, no se debe detener el reconocimiento de voz
    elif "finalizar" in texto:
        print("Deteniendo el reconocimiento de voz...")
        return False  # Indicar que se debe detener el reconocimiento de voz
    else:
        print("La palabra 'canguro' no se encontró en el texto.")
        return True  # La búsqueda de la palabra 'canguro' se ha completado, no se debe detener el reconocimiento de voz

def main():
    reconocimiento_activo = True

    while reconocimiento_activo:
        texto_reconocido = reconocer_voz()
        if texto_reconocido:
            reconocimiento_activo = buscar_palabra_canguro(texto_reconocido)

if __name__ == "__main__":
    main()
