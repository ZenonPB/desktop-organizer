from core.organizer import DesktopOrganizer
from utils.logger import setup_logger

def main():
    print("==== Desktop Organiztor V0.1 ====")

    organizer = DesktopOrganizer()
    if organizer.initialize():
        print("Organizador inicializado com sucesso.")
    else:
        print("Falha ao inicializar o organizador.")
        return

if __name__ == "__main__":
    main()