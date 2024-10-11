import os
from block import validate_block

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
        valid_blocks.sort(key=get_block_number)
        return valid_blocks[-1]  # Возвращаем последний валидный блок
    return None

def check_chain_integrity():
    """Функция для проверки целостности блокчейна."""
    files = sorted([f for f in os.listdir('blockchain') if f.endswith('.txt')], key=get_block_number)
    
    for i in range(len(files) - 1):
        current_block_number = get_block_number(files[i])
        next_block_number = get_block_number(files[i + 1])

        # Проверяем, что номера блоков идут последовательно
        if next_block_number != current_block_number + 1:
            print(f"Ошибка: Блок {current_block_number + 1} отсутствует.")
            return False
        
        # Проверяем валидность каждого блока
        if not validate_block(os.path.join('blockchain', files[i])):
            print(f"Ошибка: Блок {current_block_number} не валиден.")
            return False

    # Проверка последнего блока
    if files:
        last_block = files[-1]
        if not validate_block(os.path.join('blockchain', last_block)):
            print(f"Ошибка: Последний блок {get_block_number(last_block)} не валиден.")
            return False
    
    return True
