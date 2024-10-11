import sys
import os

def delete_block(filename):
    # Добавляем путь к папке blockchain
    filepath = os.path.join('blockchain', filename)
    
    if os.path.exists(filepath):
        os.remove(filepath)
        print(f"Блок {filename} удален.")
    else:
        print(f"Блок {filename} не найден.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Использование: python delete_block.py <имя_файла>")
        sys.exit(1)
    
    filename = sys.argv[1]
    delete_block(filename)
