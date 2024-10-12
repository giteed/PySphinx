import os
from hash_util import hash_data
from datetime import datetime

def validate_block(filepath, previous_block_hash=None):
    """Функция для валидации блока с учетом предыдущего хеша."""
    
    if os.path.exists(filepath):
        with open(filepath, 'r') as file:
            lines = file.readlines()
            
            data_line = lines[0].strip().split(": ")[1]
            stored_hash = lines[1].strip().split(": ")[1]
            previous_hash_line = lines[2].strip().split(": ")[1] if len(lines) > 2 else None
            
            # Вычисляем хеш данных
            computed_hash = hash_data(data_line)
            
            # Проверяем валидность текущего блока
            if computed_hash != stored_hash:
                print(f"Блок {filepath} не валиден. Хеши данных не совпадают.")
                return False
            
            # Если передан хеш предыдущего блока, проверяем его
            if previous_block_hash and previous_block_hash != previous_hash_line:
                print(f"Блок {filepath} не валиден. Хеш предыдущего блока не совпадает.")
                return False
            
            print(f"Блок {filepath} валиден.")
            return True
    else:
        print(f"Блок {filepath} не найден.")
        return False

def create_block(block_number, data, previous_hash=None):
    """Функция для создания нового блока."""
    if not os.path.exists('blockchain'):
        os.makedirs('blockchain')

    current_time = datetime.now()
    filename = f"blockchain/{str(block_number).zfill(6)}_{current_time.strftime('%Y-%m-%d_%H-%M-%S')}.txt"
    block_hash = hash_data(data)

    with open(filename, 'w') as file:
        file.write(f"Данные: {data}\n")
        file.write(f"Хеш: {block_hash}\n")
        if previous_hash:
            file.write(f"Хеш предыдущего блока: {previous_hash}\n")
    
    print(f"Блок {block_number} создан и сохранен в файл: {filename}")
    return block_hash  # Возвращаем хеш текущего блока, чтобы использовать его в следующем блоке

def get_block_number(filename):
    """Функция для извлечения номера блока из имени файла."""
    return int(filename.split('_')[0])

def get_last_valid_block():
    """Функция для получения последнего валидного блока."""
    files = [f for f in os.listdir('blockchain') if f.endswith('.txt')]
    valid_blocks = []

    for file in files:
        if validate_block(os.path.join('blockchain', file)):
            valid_blocks.append(file)

    if valid_blocks:
        valid_blocks.sort()
        return valid_blocks[-1]  # Возвращаем последний валидный блок
    return None

def check_chain_integrity():
    """Функция для проверки целостности блокчейна."""
    files = sorted([f for f in os.listdir('blockchain') if f.endswith('.txt')])
    previous_block_hash = None

    for i, file in enumerate(files):
        current_file = os.path.join('blockchain', file)
        if not validate_block(current_file, previous_block_hash):
            print(f"Ошибка: Блок {file} не валиден.")
            return False
        with open(current_file, 'r') as f:
            previous_block_hash = f.readlines()[1].strip().split(": ")[1]  # Берем текущий хеш как предыдущий для следующего блока
    return True
