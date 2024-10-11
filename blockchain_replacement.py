import os
import tarfile
import shutil
import hashlib
from chain import get_block_number
from hash_util import hash_data
from blockchain_info import get_next_blockchain_start  # Импортируем новый скрипт

def archive_blockchain():
    """Архивирует блокчейн, вычисляет хеш архива и создает первый блок нового блокчейна."""
    
    print("Вызов archive_blockchain()")

    # Определяем имена первого и последнего блоков
    files = [f for f in os.listdir('blockchain') if f.endswith('.txt')]
    files.sort(key=get_block_number)
    
    first_block = files[0]
    last_block = files[-1]

    # Читаем содержимое последнего блока ДО перемещения в архив
    with open(f"blockchain/{last_block}", "r") as f:
        last_block_content = f.read()

    # Извлекаем дату и время из названия файлов блоков
    first_block_datetime = '_'.join(first_block.split('_')[1:]).split('.')[0]
    last_block_datetime = '_'.join(last_block.split('_')[1:]).split('.')[0]

    # Получаем хеш последнего блока ДО перемещения файлов
    last_block_hash = hash_data(open(f"blockchain/{last_block}").readlines()[1].strip().split(": ")[1])

    # Формируем имя архива с датой и временем первого и последнего блоков
    archive_name = f"blockchain_from_{first_block_datetime}_to_{last_block_datetime}.tar.gz"
    
    # Создаем архив старого блокчейна
    print(f"Создаем архив: {archive_name}")
    with tarfile.open(archive_name, "w:gz") as tar:
        tar.add("blockchain", arcname=os.path.basename("blockchain"))
    
    print(f"Архив создан: {archive_name}")

    # Вычисляем хеш архива
    archive_hash = calculate_hash(archive_name)  # Вызов функции для вычисления хеша архива
    print(f"Хеш архива: {archive_hash}")

    # Создаем папку для архивированных блоков
    archive_folder_name = f"archive_blockchain_from_{first_block_datetime}_to_{last_block_datetime}"
    os.makedirs(archive_folder_name, exist_ok=True)

    # Перемещаем файлы блокчейна в архивную папку
    for file in files:
        shutil.move(os.path.join("blockchain", file), archive_folder_name)
    
    print(f"Файлы блокчейна перемещены в {archive_folder_name}")

    # Получаем номер для первого блока нового блокчейна
    next_block_number = get_next_blockchain_start()  # Вызов нового скрипта
    
    # Создаем первый блок нового блокчейна
    create_new_blockchain(last_block_content, last_block_hash, archive_hash, archive_name, next_block_number)

def calculate_hash(file_path):
    """Вычисляет SHA256 хеш файла."""
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

def create_new_blockchain(last_block_content, last_block_hash, archive_hash, archive_name, next_block_number):
    """Создает первый блок нового блокчейна с хешами предыдущего блокчейна."""
    print(f"Создаем первый блок нового блокчейна с номером {next_block_number}...")

    # Импортируем create_block локально внутри функции, чтобы избежать циклического импорта
    from block import create_block

    # Выводим отладочные сообщения для проверки перед созданием блока
    print(f"Отладка: Хеш последнего блока предыдущего блокчейна: {last_block_hash}")
    print(f"Отладка: Хеш архива: {archive_hash}")
    print(f"Отладка: Содержимое последнего блока предыдущего блокчейна:\n{last_block_content}")

    # Формируем данные для нового блока
    data = (f"Предыдущий блокчейн:\n"
            f"Имя архива: {archive_name}\n"
            f"Хеш архива: {archive_hash}\n"
            f"Хеш последнего блока предыдущего блокчейна: {last_block_hash}\n"
            f"====================\n"
            f"Копия последнего блока предыдущего блокчейна:\n{last_block_content}")

    # Создаем первый блок нового блокчейна с правильным номером и хешем последнего блока старого блокчейна
    create_block(next_block_number, data, previous_hash=last_block_hash)
    print(f"Первый блок нового блокчейна создан: blockchain/{str(next_block_number).zfill(6)}")
