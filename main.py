from core.organizer import DesktopOrganizer
from utils.logger import setup_logger
import sys

def main():
    print("=== Desktop Organizer ===")
    
    # Inicializar organizador
    organizer = DesktopOrganizer()
    if not organizer.initialize():
        print("❌ Falha na inicialização. Verifique os logs para detalhes.")
        sys.exit(1)
    
    # Mostrar resumo do que será feito
    print("\nResumo da operação:")
    print(f" - Desktop a ser organizado: {organizer.desktop_path}")
    print(f" - Pasta organizada: {organizer.organized_root}")
    print(f" - Total de categorias: {len(organizer.category_mapping)}")
    
    # Solicitar confirmação
    confirm = input("\nDeseja prosseguir com a organização? (s/n): ").strip().lower()
    if confirm != 's':
        print("Operação cancelada pelo usuário.")
        sys.exit(0)
    
    # Executar organização
    print("\nOrganizando arquivos...")
    if organizer.organize():
        print("✅ Organização concluída com sucesso!")
    else:
        print("❌ Ocorreram erros durante a organização. Verifique os logs.")
    
    input("\nPressione Enter para sair...")

if __name__ == "__main__":
    main()