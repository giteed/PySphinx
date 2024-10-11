import os
from hash_util import hash_data
from datetime import datetime

def validate_block(filename):
    """Функция для валидации блока."""
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            lines = file.readlines()
            data_line = lines[0].strip().split(": ")[1]
            stored_hash = lines[1].strip().split(": ")[1]
            previous_hash = lines[2].strip().split(": ")[1] if len(lines) > 2 else None
            
            # Вычисляем хеш данных
            computed_hash = hash_data(data_line)
            
            return computed_hash == stored_hash
    return False

from blockchain_replacement import archive_blockchain

def create_block(block_number, data, previous_hash=None):
    """Функция для создания нового блока."""
    if not os.path.exists('blockchain'):
        os.makedirs('blockchain')

    current_time = datetime.now()
    filename = f"blockchain/{str(block_number).zfill(6)}_{current_time.strftime('%Y-%m-%d_%H-%M-%S')}.txt"
    block_hash = hash_data(data)

    print(f"Отладка: создаем блок {block_number}")
    print(f"Отладка: данные блока: {data}")
    print(f"Отладка: хеш блока: {block_hash}")
    if previous_hash:
        print(f"Отладка: хеш предыдущего блока: {previous_hash}")

    with open(filename, 'w') as file:
        file.write(f"Данные: {data}\n")
        file.write(f"Хеш: {block_hash}\n")
        if previous_hash:
            file.write(f"Хеш предыдущего блока: {previous_hash}\n")
    
    print(f"Блок {block_number} создан и сохранен в файл: {filename}")
