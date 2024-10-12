@echo off
set VENV=env
set REPO_URL=https://github.com/giteed/PySphinx.git
set PROJECT_DIR=PySphinx

:: Проверка наличия Git
where git >nul 2>nul
if %ERRORLEVEL% NEQ 0 (
    echo Git не установлен. Пожалуйста, установите Git и повторите попытку.
    exit /b
)

:: 1. Клонирование или обновление репозитория
if exist "%PROJECT_DIR%" (
    echo Проект уже существует. Проверяем обновления...
    cd %PROJECT_DIR%
    git pull origin master
) else (
    echo Клонируем проект...
    git clone %REPO_URL%
    cd %PROJECT_DIR%
)

:: Проверка наличия Python
where python >nul 2>nul
if %ERRORLEVEL% NEQ 0 (
    echo Python не установлен. Пожалуйста, установите Python и повторите попытку.
    exit /b
)

:: 2. Создание виртуального окружения, если оно не существует
if not exist "%VENV%" (
    echo Создаем виртуальное окружение...
    python -m venv %VENV%
)

:: 3. Активация виртуального окружения
echo Активируем виртуальное окружение...
call %VENV%\Scripts\activate

:: 4. Установка зависимостей
echo Устанавливаем зависимости...
pip install --upgrade pip
pip install -r requirements.txt

:: 5. Создание папки blockchain, если она не существует
if not exist "blockchain" (
    echo Создаем папку blockchain...
    mkdir blockchain
)

:: 6. Запуск основного файла PySphinx.py
echo Запускаем PySphinx.py...
python PySphinx.py

:: Завершаем выполнение
echo Завершено.
pause
