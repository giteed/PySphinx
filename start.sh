#!/bin/bash

# Название виртуального окружения
VENV="env"
REPO_URL="https://github.com/giteed/PySphinx.git"
PROJECT_DIR="PySphinx"

# Проверка, установлен ли Git
if ! command -v git &> /dev/null
then
    echo "Git не установлен. Пожалуйста, установите Git и повторите попытку."
    exit
fi

# 1. Клонирование или обновление репозитория
if [ -d "$PROJECT_DIR" ]; then
    echo "Проект уже существует. Проверяем обновления..."
    cd "$PROJECT_DIR"
    git pull origin master
else
    echo "Клонируем проект..."
    git clone "$REPO_URL"
    cd "$PROJECT_DIR"
fi

# 2. Проверка наличия Python и виртуального окружения
if ! command -v python3 &> /dev/null
then
    echo "Python3 не установлен. Пожалуйста, установите Python3 и повторите попытку."
    exit
fi

# 3. Создание виртуального окружения, если оно не существует
if [ ! -d "$VENV" ]; then
    echo "Создаем виртуальное окружение..."
    python3 -m venv "$VENV"
fi

# 4. Активация виртуального окружения
echo "Активируем виртуальное окружение..."
# Для Linux/macOS
source "$VENV/bin/activate"

# Для Windows используйте:
# source "$VENV/Scripts/activate"

# 5. Проверка и установка зависимостей
echo "Проверяем зависимости..."
pip install --upgrade pip
pip install -r requirements.txt

# 6. Создание папки blockchain, если она не существует
if [ ! -d "blockchain" ]; then
    echo "Создаем папку blockchain..."
    mkdir blockchain
fi

# 7. Запуск основного файла PySphinx.py
echo "Запускаем PySphinx.py..."
python PySphinx.py
