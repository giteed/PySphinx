import os
from block import validate_block

def validate_all_blocks():
    """Функция для валидации всех блоков."""
    files = [f for f in os.listdir('blockchain') if f.endswith('.txt')]
    all_valid = True

    for file in files:
        if not validate_block(os.path.join('blockchain', file)):
            print(f"Блок {file} не валиден.")
            all_valid = False
        else:
            print(f"Блок {file} валиден.")

    return all_valid

if __name__ == "__main__":
    if validate_all_blocks():
        print("Все блоки валидны.")
    else:
        print("Обнаружены невалидные блоки.")
