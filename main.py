import speech_recognition as sr
import subprocess
import time
import pyttsx3

def escuchar_comandos():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    with mic as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Escuchando...")
        audio = recognizer.listen(source)

    try:
        comando = recognizer.recognize_google(audio, language='es-ES')
        print("Comando reconocido:", comando)
        return comando.lower()
    except sr.UnknownValueError:
        print("No se pudo entender el comando")
        return None
    except sr.RequestError as e:
        print("Error en la solicitud al servicio de reconocimiento de voz; {0}".format(e))
        return None

def ejecutar_run_py():
    print("Ejecutando run.py...")
    subprocess.Popen(["python", "run.py"])

def ejecutar_close_py():
    print("Ejecutando close.py...")
    subprocess.Popen(["python", "close.py"])

def hablar(texto):
    engine = pyttsx3.init()
    engine.say(texto)
    engine.runAndWait()

def main():
    while True:
        comando = escuchar_comandos()

        if comando == "canguro":
            hablar("ABRIENDO NAVEGADOR...")
            ejecutar_run_py()

            while True:
                comando = escuchar_comandos()
                if comando == "detener":
                    ejecutar_close_py()
                    hablar("Se ha detenido el proceso")
                    print("Desconectando...")
                    print("Desconexión completa")
                    time.sleep(2)  # Esperamos 2 segundos
                    return  # Salimos de la función main() cuando se completa la desconexión

if __name__ == "__main__":
    main()
