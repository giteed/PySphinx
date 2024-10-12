import os
from validate_block import validate_block

def validate_all_blocks():
    """Функция для валидации всех блоков."""
    
    files = [f for f in os.listdir('blockchain') if f.endswith('.txt')]
    files.sort()  # Убедимся, что блоки проверяются по порядку

    all_valid = True
    previous_block_hash = None

    for file in files:
        # Проверяем каждый блок, передавая хеш предыдущего блока для проверки
        if not validate_block(os.path.join('blockchain', file), previous_block_hash):
            all_valid = False
        else:
            # Считываем текущий хеш как предыдущий для следующей итерации
            with open(os.path.join('blockchain', file), 'r') as f:
                previous_block_hash = f.readlines()[1].strip().split(": ")[1]

    return all_valid

if __name__ == "__main__":
    if validate_all_blocks():
        print("Все блоки валидны.")
    else:
        print("Обнаружены невалидные блоки.")
