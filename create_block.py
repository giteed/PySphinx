import sys
from block import create_block
from chain import get_last_valid_block, check_chain_integrity, get_block_number
from hash_util import hash_data
from datetime import datetime
import os
from colorama import Fore, Style, init

# Инициализация цветного вывода
init(autoreset=True)

def print_block_stats():
    """Функция для вывода статистики блоков, отсортированных по номеру."""
    files = [f for f in os.listdir('blockchain') if f.endswith('.txt')]
    
    if not files:
        print(Fore.RED + "Нет созданных блоков.")
        return

    # Сортируем файлы по номеру блока
    files.sort(key=get_block_number)

    print(Fore.CYAN + "=== Статистика по блокам ===")
    for file in files:
        filepath = os.path.join('blockchain', file)
        with open(filepath, 'r') as f:
            lines = f.readlines()
            block_number = get_block_number(file)
            data = lines[0].strip().split(": ")[1]
            block_hash = lines[1].strip().split(": ")[1]
            prev_hash = lines[2].strip().split(": ")[1] if len(lines) > 2 else "None"

            # Выводим информацию о блоке
            print(f"{Fore.YELLOW}Блок №{block_number}")
            print(f"  {Fore.GREEN}Хеш блока: {block_hash}")
            print(f"  {Fore.BLUE}Хеш предыдущего блока: {prev_hash}")
            print(f"  {Fore.MAGENTA}Данные: {data}")

    print(Fore.CYAN + "============================")

if __name__ == "__main__":
    # Проверка целостности перед созданием нового блока
    if not check_chain_integrity():
        print(Fore.RED + "Обнаружены ошибки в цепочке блоков. Создание нового блока невозможно.")
        sys.exit(1)
    
    # Выводим статистику перед созданием нового блока
    print_block_stats()

    last_valid_block = get_last_valid_block()
    
    if last_valid_block:
        print(f"Последний валидный блок: {last_valid_block}")
        last_block_number = int(last_valid_block.split('_')[0]) + 1
    else:
        print("Нет валидных блоков. Начинаем с блока 1.")
        last_block_number = 1

    if len(sys.argv) > 2:
        data = sys.argv[2]
    else:
        data = input("Введите данные для нового блока: ")

    previous_hash = hash_data(open(f"blockchain/{last_valid_block}").readlines()[1].strip().split(": ")[1]) if last_valid_block else None
    create_block(last_block_number, data, previous_hash)
