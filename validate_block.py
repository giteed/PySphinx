import sys
import os
import hashlib

def hash_data(data):
    """Функция для хеширования данных блока."""
    return hashlib.sha256(data.encode()).hexdigest()

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
