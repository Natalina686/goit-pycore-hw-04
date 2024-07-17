import os
from colorama import Fore, Style

def visualize_directory_structure(directory_path, indent=''):
    try:
        for item in os.listdir(directory_path):
            item_path = os.path.join(directory_path, item)
            if os.path.isfile(item_path):
                print(f"{indent}{Fore.BLUE}{item}{Style.RESET_ALL}")  # ім'я файлу синім кольором
            elif os.path.isdir(item_path):
                print(f"{indent}{Fore.GREEN}{item}{Style.RESET_ALL}")  # ім'я директорії зеленим кольором
                visualize_directory_structure(item_path, indent + '  ')  # Рекурсивно викликати функцію для піддиректорій
    except FileNotFoundError:
        print("Директорію не знайдено")
    except Exception as e:
        print(f"Сталася помилка: {e}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Будь ласка, вкажіть шлях до директорії")
    else:
        directory_path = sys.argv[1]
        if not os.path.isdir(directory_path):
            print("Вказаний шлях не є директорією")
        else:
            visualize_directory_structure(directory_path)