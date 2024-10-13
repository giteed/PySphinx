import os
from block import validate_block

def get_block_number(filename):
    """Функция для извлечения номера блока из имени файла."""
    return int(filename.split('_')[0])

def check_chain_integrity():
    """Функция для проверки целостности блокчейна."""
    files = sorted([f for f in os.listdir('blockchain') if f.endswith('.txt')], key=get_block_number)
    
    if not files:
        print("Нет доступных блоков.")
        return True
    
    previous_hash = None
    for i in range(len(files)):
        current_block_number = get_block_number(files[i])

        # Проверяем валидность каждого блока
        if i == 0 and "Предыдущий блокчейн" in open(f'blockchain/{files[i]}').read():
            # Если это первый блок нового блокчейна, проверяем его по хешу архива
            archive_hash = extract_archive_hash_from_block(files[i])
            if not validate_block(os.path.join('blockchain', files[i]), archive_hash):
                print(f"Ошибка: Блок {current_block_number} не валиден (хеш архива не совпадает).")
                return False
        else:
            # Обычная проверка хеша предыдущего блока для остальных блоков
            if not validate_block(os.path.join('blockchain', files[i]), previous_hash):
                print(f"Ошибка: Блок {current_block_number} не валиден.")
                return False
        
        # Обновляем хеш для следующего блока
        previous_hash = extract_block_hash(files[i])

    print("Цепочка блоков валидна.")
    return True

def extract_block_hash(filename):
    """Извлекает хеш блока из файла."""
    with open(f'blockchain/{filename}', 'r') as file:
        lines = file.readlines()
        return lines[1].strip().split(": ")[1]

def extract_archive_hash_from_block(filename):
    """Извлекает хеш архива из первого блока нового блокчейна."""
    with open(f'blockchain/{filename}', 'r') as file:
        lines = file.readlines()
        return lines[2].strip().split(": ")[1]
