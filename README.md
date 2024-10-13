# PySphinx
Создание, поддержание и валидация простой, но функциональной блокчейн-системы, которая может работать на локальном уровне.

### Название проекта: **PySphinx**
![PySphinx](images/MarkuryFLUX_00570_.png)
### Описание проекта:

**Цель проекта**:  
Цель проекта — создание, поддержание и валидация простой, но функциональной блокчейн-системы, которая может работать на локальном уровне. Эта система создает и хранит блоки с данными, проверяет целостность блоков и позволяет беспрерывно создавать новые блоки, даже после того, как лимит блоков в текущем блокчейне исчерпан (лимит в 9999 блоков). После завершения блокчейна старые блоки архивируются, и создается новый блокчейн, который продолжает цепочку.

Проект **PySphinx** предлагает гибкую, но надежную систему для создания и управления локальным блокчейном. Система поддерживает непрерывную цепочку блоков, автоматическую архивацию и проверку целостности данных, что делает ее подходящей для обучения или разработки на основе базовой блокчейн-технологии.

**Основные задачи**:
- Надежное создание блоков с данными, хешами и ссылками на предыдущие блоки.
- Валидация блоков для сохранения целостности блокчейна.
- Архивация блоков после достижения лимита в 9999 блоков.
- Создание нового блокчейна с сохранением информации о предыдущем для продолжения цепочки.


### Установка на Linux/macOS

Для установки проекта на Linux или macOS, выполните следующую команду в терминале:

```bash
wget https://raw.githubusercontent.com/giteed/PySphinx/main/start.sh && chmod +x start.sh && ./start.sh
```

### Установка на Windows

Для установки проекта на Windows выполните следующую команду в командной строке (CMD):

```bat
curl -o start.bat https://raw.githubusercontent.com/giteed/PySphinx/main/start.bat && start.bat
```

---

### Описание:

1. **Linux/macOS**:
   - **wget** скачивает скрипт `start.sh`.
   - **chmod +x** делает скрипт исполняемым.
   - **./start.sh** запускает скрипт, который:
     - Клонирует или обновляет репозиторий.
     - Создает виртуальное окружение и устанавливает зависимости.
     - Создает папку `blockchain/`, если она отсутствует.
     - Запускает основной скрипт `PySphinx.py`.

2. **Windows**:
   - **curl** скачивает скрипт `start.bat`.
   - **start.bat** запускает скрипт, который:
     - Клонирует или обновляет проект.
     - Создает виртуальное окружение и устанавливает необходимые зависимости.
     - Создает папку `blockchain/`, если она отсутствует.
     - Запускает основной файл `PySphinx.py`.

---

### Как использовать:

1. Скопируйте соответствующую команду для вашей операционной системы.
2. Вставьте её в терминал (Linux/macOS) или командную строку (Windows).
3. Нажмите **Enter** — скрипт автоматически выполнит все необходимые действия по установке и запуску проекта.

Этот процесс обеспечивает удобную установку проекта без необходимости ручной настройки.




### Структура проекта:

Проект состоит из нескольких скриптов, каждый из которых выполняет определенную роль в создании, управлении и валидации блоков в блокчейне.

---

#### 1. **`create_block.py`**
**Функционал**: 
Этот скрипт отвечает за создание нового блока в текущем блокчейне. Перед созданием нового блока система проверяет целостность всей цепочки блоков и валидность последнего блока. Если валидация проходит успешно, новый блок создается, используя данные пользователя и хеш предыдущего блока.

**Ключевые функции**:
- Проверка целостности цепочки через вызов функций валидации.
- Создание нового блока и сохранение его в файл с уникальным именем.
- Если блокчейн достигает лимита в 9999 блоков, вызывается процесс архивирования и создания нового блокчейна.

---

#### 2. **`block.py`**
**Функционал**: 
Этот файл содержит основные функции для создания и валидации блоков. Блоки создаются с учетом данных пользователя, хеша блока и хеша предыдущего блока. Хеш блоков вычисляется с использованием алгоритма SHA-256, чтобы обеспечить безопасность данных и целостность цепочки.

**Ключевые функции**:
- `create_block`: Создает новый блок с хешем данных и ссылкой на предыдущий блок.
- `validate_block`: Валидирует блок, проверяя его хеш и хеш предыдущего блока.

---

#### 3. **`chain.py`**
**Функционал**: 
Содержит функции для работы с цепочкой блоков. Скрипт отвечает за проверку целостности цепочки и получение последнего валидного блока.

**Ключевые функции**:
- `check_chain_integrity`: Проверяет, что все блоки в цепочке идут последовательно и что каждый блок валиден.
- `get_last_valid_block`: Возвращает последний валидный блок в цепочке.

---

#### 4. **`validate_block.py`**
**Функционал**: 
Скрипт для валидации конкретного блока. Пользователь может запустить его для проверки конкретного блока по его имени.

**Ключевые функции**:
- `validate_block`: Проверяет, что хеш блока совпадает с вычисленным хешем данных и что хеш предыдущего блока соответствует ожиданиям.

---

#### 5. **`validate_chain.py`**
**Функционал**: 
Скрипт для полной валидации всех блоков в текущем блокчейне. Он проходит по каждому блоку в цепочке и проверяет их целостность, начиная с первого и заканчивая последним.

**Ключевые функции**:
- `validate_all_blocks`: Проверяет, что каждый блок валиден и что хеши данных и предыдущих блоков совпадают.

---

#### 6. **`blockchain_replacement.py`**
**Функционал**: 
Этот скрипт отвечает за архивирование старого блокчейна и создание нового после достижения лимита в 9999 блоков. Он архивирует файлы блокчейна, перемещает их в архивную папку, вычисляет хеш архива, а затем создает новый блокчейн, который продолжает цепочку.

**Ключевые функции**:
- `archive_blockchain`: Архивирует текущий блокчейн, перемещает блоки в архив и создает хеш архива.
- `calculate_hash`: Вычисляет хеш архива с помощью алгоритма SHA-256.
- `create_new_blockchain`: Создает первый блок нового блокчейна с информацией о предыдущем блокчейне, включая хеши и метаданные архива.

---

#### 7. **`blockchain_info.py`**
**Функционал**: 
Этот вспомогательный скрипт собирает информацию о существующих архивированных блокчейнах, чтобы можно было корректно определить, с какого номера должен начинаться следующий блокчейн.

**Ключевые функции**:
- `get_existing_blockchains`: Собирает информацию о существующих блокчейнах.
- `get_next_blockchain_start`: Определяет номер для первого блока в новом блокчейне, основываясь на предыдущем архивированном блокчейне.

---

#### 8. **`test_blockchain.py`**
**Функционал**: 
Тестовый скрипт, который автоматически создает блоки для тестирования блокчейна. Он генерирует случайные данные для блоков и добавляет их в цепочку до тех пор, пока не будет достигнут лимит блоков, после чего тестирует процесс архивирования и создания нового блокчейна.

**Ключевые функции**:
- `create_test_blockchain`: Генерирует случайные блоки для тестирования цепочки и процесса создания нового блокчейна.

---

### Логика работы проекта:

1. **Создание блоков**:
   - Каждый новый блок содержит данные, хеш этих данных и хеш предыдущего блока.
   - Блоки хранятся в текстовых файлах в папке `blockchain`, и каждый файл имеет уникальное имя, включающее номер блока и временную метку.

2. **Проверка целостности**:
   - Перед созданием каждого нового блока проверяется целостность всей цепочки. Если хотя бы один блок не проходит проверку, система выдает ошибку и не позволяет создавать новый блок.

3. **Архивирование**:
   - Когда количество блоков в текущем блокчейне достигает лимита (9999 блоков), система автоматически архивирует старые блоки, вычисляет их хеш и перемещает в архивную папку. Затем создается новый блокчейн, который продолжает цепочку с новым номером блока.

4. **Непрерывность цепочки**:
   - При создании первого блока нового блокчейна в него включается информация о предыдущем блокчейне, включая хеш последнего блока и хеш архива, что обеспечивает непрерывность цепочки.

5. **Валидация**:
   - В любой момент времени пользователь может запустить проверку цепочки, чтобы убедиться в том, что все блоки валидны и целостность данных не нарушена.

### Скрипты для установки и запуска проекта

Для автоматической установки, настройки, обновления и запуска проекта доступны два скрипта:

1. **`start.sh` (для Linux/macOS)**  
2. **`start.bat` (для Windows)**  

#### Описание действий скриптов:

1. **Клонирование или обновление репозитория**:  
   Если проект уже клонирован на локальный компьютер, скрипт проверяет наличие обновлений с помощью `git pull`. Если проекта еще нет, он будет клонирован с репозитория.

2. **Создание и активация виртуального окружения**:  
   Скрипт проверяет наличие виртуального окружения. Если оно отсутствует, создается новое виртуальное окружение, которое затем активируется. Если окружение уже существует, оно просто активируется.

3. **Проверка и установка зависимостей**:  
   Скрипт проверяет наличие всех необходимых зависимостей, указанных в файле `requirements.txt`. Если какие-то зависимости отсутствуют, они будут автоматически установлены.

4. **Создание директории `blockchain/`**:  
   Скрипт проверяет наличие папки `blockchain/`, в которой будут храниться все блоки. Если папка отсутствует, она будет создана.

5. **Запуск основного файла `PySphinx.py`**:  
   После настройки проекта и активации виртуального окружения скрипт автоматически запускает основной файл проекта `PySphinx.py`, который предоставляет пользователю меню для управления блокчейном.


### Системные требования

Для корректной установки и работы проекта **PySphinx** необходимо следующее:

#### Минимальные требования:
1. **Операционная система**: 
   - Windows 10/11
   - Linux (Ubuntu, Debian, CentOS и т.д.)
   - macOS 10.13 и выше
2. **Python**: Версия 3.6 и выше
3. **Доступ к интернету**: Для клонирования репозитория и установки зависимостей.
4. **Свободное дисковое пространство**: Минимум 500 MB для установки проекта и хранения данных, но для долгосрочной работы может потребоваться больше в зависимости от количества блоков в блокчейне.

#### Дополнительные требования:
- **Git**: Для клонирования репозитория и обновления проекта.
- **Виртуальное окружение Python**: Для изоляции зависимости проекта (создается автоматически при установке).

### Оценка дискового пространства

Пользователь должен самостоятельно оценивать потребность в дисковом пространстве для хранения данных блокчейна. Объем, требуемый для хранения блоков, зависит от следующих факторов:
- Количество блоков.
- Размер данных внутри каждого блока.
  
Каждый блок сохраняется в текстовом файле, и блокчейн может значительно вырасти по объему в зависимости от того, как часто создаются новые блоки и сколько данных записано в каждый блок.

### Управление старыми блоками

После архивирования блокчейна проект автоматически сохраняет архив, содержащий все блоки в упакованном виде. Пользователь может удалить файлы старого блокчейна, чтобы освободить место, если они уже не нужны в их первоначальном виде. Это можно сделать, если:
- **Файлы были архивированы**: После успешного архивирования блоков в `.tar.gz` архиве можно безопасно удалить оригинальные текстовые файлы, чтобы освободить место.
  
> **Важно:** Убедитесь, что архив создан корректно и сохранен в надежном месте перед удалением исходных файлов блокчейна.

### Заключение

Вот исправленное сообщение с учетом ваших уточнений:

---

**Заключение**

Проект PySphinx требует умеренного объема системных ресурсов и дискового пространства, но пользователю важно учитывать, как будет расти объем данных в зависимости от использования блокчейна. Очистка и архивирование старых блоков может значительно уменьшить нагрузку на дисковое пространство.

В процессе смены блокчейна на диске образуются архивированные и перемещенные файлы старого блокчейна в папке `blockchain_tar_gz`. Размер этого блокчейна в этой папке может увеличиваться в 2 раза, поэтому пользователю необходимо самостоятельно регулировать этот процесс. Рекомендуется периодически проверять и удалять старые папки с блокчейном, которые больше не нужны, чтобы избежать переполнения диска и связанных с этим проблем с местом на сервере. Архивы, созданные из этих папок, удалять нельзя, так как они содержат важные данные архивированных ранее блокчейнов цепочки.

---



