import os
import re

def get_existing_blockchains():
    """Собирает информацию о существующих архивированных блокчейнах."""
    # Находим архивы блокчейнов
    archives = [f for f in os.listdir('.') if f.startswith("blockchain_from_") and f.endswith(".tar.gz")]
    
    # Если архивов нет
    if not archives:
        print("Нет существующих архивов блокчейнов.")
        return None
    
    # Сортируем архивы по времени создания (по названию)
    archives.sort()
    
    # Находим последний архив
    last_archive = archives[-1]
    
    # Извлекаем информацию из имени архива
    match = re.search(r'blockchain_from_(\d{4}-\d{2}-\d{2}_\d{2}-\d{2}-\d{2})_to_(\d{4}-\d{2}-\d{2}_\d{2}-\d{2}-\d{2})', last_archive)
    
    if match:
        first_block_datetime = match.group(1)
        last_block_datetime = match.group(2)
        
        # Печатаем информацию
        print(f"Последний архивированный блокчейн: {last_archive}")
        print(f"Дата и время первого блока: {first_block_datetime}")
        print(f"Дата и время последнего блока: {last_block_datetime}")
        
        # Возвращаем информацию о последнем блоке предыдущего блокчейна
        return last_block_datetime
    else:
        print("Ошибка: не удалось извлечь информацию из имени архива.")
        return None

def get_next_blockchain_start():
    """Определяет номер для первого блока нового блокчейна."""
    last_block_datetime = get_existing_blockchains()
    
    if last_block_datetime:
        # Находим номер последнего блока из предыдущего блокчейна
        last_block_number = 99999  # Число блоков в одном блокчейне, начиная с 00001
        return last_block_number + 1  # Новый блок начнется с 100000
    else:
        return 1  # Если архивов нет, начинаем с 1

if __name__ == "__main__":
    next_block_number = get_next_blockchain_start()
    print(f"Следующий номер блока: {str(next_block_number).zfill(6)}")
