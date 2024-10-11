import sys
import os
import hashlib

def hash_data(data):
    """Функция для хеширования данных блока."""
    return hashlib.sha256(data.encode()).hexdigest()

def validate_block(filename, previous_block_hash=None):
    """Функция для валидации блока с опцией проверки предыдущего блока."""
    
    # Добавляем путь к папке blockchain
    filepath = os.path.join('blockchain', filename)
    
    if os.path.exists(filepath):
        with open(filepath, 'r') as file:
            lines = file.readlines()
            data_line = lines[0].strip().split(": ")[1]
            stored_hash = lines[1].strip().split(": ")[1]
            
            # Вычисляем хеш данных
            computed_hash = hash_data(data_line)

            # Отладка: выводим данные для сравнения хеша
            print(f"Отладка: проверка блока {filename}")
            print(f"Отладка: данные блока: {data_line}")
            print(f"Отладка: хеш, хранящийся в блоке: {stored_hash}")
            print(f"Отладка: вычисленный хеш данных: {computed_hash}")
            
            if computed_hash == stored_hash:
                if previous_block_hash:
                    # Проверяем хеш предыдущего блока
                    prev_hash_in_block = lines[2].strip().split(": ")[1]
                    print(f"Отладка: хеш предыдущего блока в блоке: {prev_hash_in_block}")
                    print(f"Отладка: ожидаемый хеш предыдущего блока: {previous_block_hash}")
                    if prev_hash_in_block != previous_block_hash:
                        print(f"Блок {filename} не валиден. Хеш предыдущего блока не совпадает.")
                        return False
                print(f"Блок {filename} валиден.")
                return True
            else:
                print(f"Блок {filename} не валиден. Хеши не совпадают.")
                return False
    else:
        print(f"Блок {filename} не найден.")
        return False
