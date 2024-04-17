import psutil

def cerrar_edge():
    for proc in psutil.process_iter():
        try:
            # Verificar si el proceso es de Microsoft Edge
            if "msedge" in proc.name():
                # Cerrar el proceso
                proc.kill()
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

def main():
    cerrar_edge()

if __name__ == "__main__":
    main()
