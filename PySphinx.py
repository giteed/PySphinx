import os
import subprocess

def display_menu():
    print("=== Меню управления ChainMaster 9999 ===")
    print("1. Создать новый блок")
    print("2. Проверить целостность всех блоков")
    print("3. Валидация конкретного блока")
    print("4. Показать все блоки")
    print("5. Завершить и архивировать текущий блокчейн")
    print("6. Выход")

def create_block():
    os.system("python create_block.py")

def validate_chain():
    os.system("python validate_chain.py")

def validate_block():
    block_file = input("Введите имя файла блока для валидации: ")
    os.system(f"python validate_block.py {block_file}")

def list_blocks():
    os.system("python list_blocks.py")

def archive_blockchain():
    os.system("python create_block.py")  # Последний блок запустит архивирование

def main():
    while True:
        display_menu()
        choice = input("Выберите действие (1-6): ")

        if choice == "1":
            create_block()
        elif choice == "2":
            validate_chain()
        elif choice == "3":
            validate_block()
        elif choice == "4":
            list_blocks()
        elif choice == "5":
            archive_blockchain()
        elif choice == "6":
            print("Выход из программы...")
            break
        else:
            print("Некорректный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()
