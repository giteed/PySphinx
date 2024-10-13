import os
import tarfile
import shutil
import hashlib
import random
import humanize  # Для вывода размера архива в человеко-читаемом формате
from colorama import Fore, Style, init  # Для цветного вывода
from chain import get_block_number
from hash_util import hash_data
from blockchain_info import get_next_blockchain_start
from datetime import datetime

# Инициализация цветного вывода
init(autoreset=True)

def generate_blockchain_id():
    """Генерирует 8-значный уникальный ID для блокчейна."""
    return ''.join([str(random.randint(0, 9)) for _ in range(8)])

def get_human_readable_size(filepath):
    """Возвращает размер файла в человеко-читаемом формате (MB/GB)."""
    size_bytes = os.path.getsize(filepath)
    return humanize.naturalsize(size_bytes)

def archive_blockchain():
    """Архивирует блокчейн, вычисляет хеш архива и создает первый блок нового блокчейна."""
    
    print(Fore.YELLOW + "Достигнут лимит в 9999 блоков. Запускаем архивирование...")

    # Определяем имена первого и последнего блоков
    files = [f for f in os.listdir('blockchain') if f.endswith('.txt')]
    files.sort(key=get_block_number)
    
    first_block = files[0]
    last_block = files[-1]

    # Генерация уникального ID для блокчейна
    blockchain_id = generate_blockchain_id()

    # Читаем содержимое последнего блока ДО перемещения в архив
    with open(f"blockchain/{last_block}", "r") as f:
        last_block_content = f.read()

    # Извлекаем дату и время из названия файлов блоков
    first_block_datetime = '_'.join(first_block.split('_')[1:]).split('.')[0]
    last_block_datetime = '_'.join(last_block.split('_')[1:]).split('.')[0]

    # Получаем хеш последнего блока ДО перемещения файлов
    last_block_hash = hash_data(open(f"blockchain/{last_block}").readlines()[1].strip().split(": ")[1])

    # Формируем имя архива с номером блоков и датами
    archive_folder = 'blockchain_tar_gz'
    if not os.path.exists(archive_folder):
        os.makedirs(archive_folder)

    archive_name = f"{archive_folder}/blockchain_{blockchain_id}_000000_009999_from_{first_block_datetime}_to_{last_block_datetime}.tar.gz"
    
    # Создаем архив старого блокчейна
    print(Fore.YELLOW + f"Создаем архив: {archive_name}")
    with tarfile.open(archive_name, "w:gz") as tar:
        tar.add("blockchain", arcname=os.path.basename("blockchain"))
    
    print(Fore.GREEN + f"Архив создан: {archive_name}")

    # Вычисляем хеш архива
    archive_hash = calculate_hash(archive_name)
    print(Fore.CYAN + f"Хеш архива: {archive_hash}")

    # Создаем папку для архивированных блоков внутри blockchain_tar_gz
    archive_folder_name = f"{archive_folder}/archive_blockchain_{blockchain_id}_000000_009999_from_{first_block_datetime}_to_{last_block_datetime}"
    os.makedirs(archive_folder_name, exist_ok=True)

    # Перемещаем файлы блокчейна в архивную папку
    for file in files:
        shutil.move(os.path.join("blockchain", file), archive_folder_name)
    
    print(Fore.BLUE + f"Файлы блокчейна перемещены в {archive_folder_name}")

    # Получаем размер архива
    archive_size = get_human_readable_size(archive_name)

    # Создаем папку для логов, если её нет
    logs_folder = "logs"
    if not os.path.exists(logs_folder):
        os.makedirs(logs_folder)

    # Лог-файл для архивации
    log_filename = f"{logs_folder}/blockchain_replacement_{blockchain_id}_000000_009999.log"
    with open(log_filename, "w") as log_file:
        log_file.write(f"Архив: {archive_name}\n")
        log_file.write(f"Хеш архива: {archive_hash}\n")
        log_file.write(f"Размер архива: {archive_size}\n")
        log_file.write(f"Первый блок: {first_block}\n")
        log_file.write(f"Последний блок: {last_block}\n")
        log_file.write(f"Файлы блокчейна перемещены в: {archive_folder_name}\n")

    print(Fore.GREEN + f"Лог сохранён: {log_filename}")

    # Получаем номер для первого блока нового блокчейна
    next_block_number = get_next_blockchain_start()
    
    # Создаем первый блок нового блокчейна
    create_new_blockchain(last_block_content, last_block_hash, archive_hash, archive_name, next_block_number, blockchain_id)

def calculate_hash(file_path):
    """Вычисляет SHA256 хеш файла."""
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

def create_new_blockchain(last_block_content, last_block_hash, archive_hash, archive_name, next_block_number, blockchain_id):
    """Создает первый блок нового блокчейна с хешами предыдущего блокчейна."""
    print(Fore.YELLOW + f"Создаем первый блок нового блокчейна с номером {next_block_number}...")

    from block import create_block

    data = (f"Предыдущий блокчейн:\n"
            f"Имя архива: {archive_name}\n"
            f"Хеш архива: {archive_hash}\n"
            f"Хеш последнего блока предыдущего блокчейна: {last_block_hash}\n"
            f"====================\n"
            f"Копия последнего блока предыдущего блокчейна:\n{last_block_content}")

    create_block(next_block_number, data, previous_hash=last_block_hash)
    print(Fore.GREEN + f"Первый блок нового блокчейна создан: blockchain/{str(next_block_number).zfill(6)}")
