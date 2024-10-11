import os
from block import validate_block
from blockchain_info import get_existing_blockchains  # Импортируем наш новый скрипт

def get_last_block_of_previous_chain():
    """Получает последний блок предыдущего блокчейна из информации о существующих архивах."""
    last_block_datetime = get_existing_blockchains()
    
    if last_block_datetime:
        # Формируем имя последнего блока предыдущего блокчейна (например, 09999)
        last_block_number = "09999"  # Если знаем, что блокчейн заканчивается на 99999
        last_block_filename = f"{last_block_number}_{last_block_datetime}.txt"
        archive_folder_name = f"archive_blockchain_from_..._to_{last_block_datetime}"
        return os.path.join(archive_folder_name, last_block_filename)
    return None

def validate_all_blocks():
    """Функция для валидации всех блоков, включая первый блок нового блокчейна."""
    files = [f for f in os.listdir('blockchain') if f.endswith('.txt')]
    all_valid = True

    # Попробуем получить последний блок из предыдущего блокчейна
    previous_block_hash = None
    last_block_of_previous_chain = get_last_block_of_previous_chain()
    
    if last_block_of_previous_chain and os.path.exists(last_block_of_previous_chain):
        # Валидация последнего блока предыдущего блокчейна
        print(f"Валидация последнего блока предыдущего блокчейна: {last_block_of_previous_chain}")
        if not validate_block(last_block_of_previous_chain):
            print(f"Последний блок предыдущего блокчейна не валиден: {last_block_of_previous_chain}")
            all_valid = False
        else:
            # Получаем хеш последнего блока для проверки первого блока нового блокчейна
            with open(last_block_of_previous_chain, 'r') as file:
                lines = file.readlines()
                previous_block_hash = lines[1].strip().split(": ")[1]  # Хеш предыдущего блока

    # Валидация блоков нового блокчейна
    for file in sorted(files):
        print(f"Валидация блока: {file}")
        if not validate_block(os.path.join('blockchain', file), previous_block_hash):
            print(f"Блок {file} не валиден.")
            all_valid = False
        else:
            # Обновляем хеш для следующего блока
            with open(os.path.join('blockchain', file), 'r') as f:
                lines = f.readlines()
                previous_block_hash = lines[1].strip().split(": ")[1]  # Обновляем хеш для следующей валидации

    return all_valid

if __name__ == "__main__":
    if validate_all_blocks():
        print("Все блоки валидны.")
    else:
        print("Обнаружены невалидные блоки.")
