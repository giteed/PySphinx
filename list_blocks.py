import os

def list_blocks():
    # Изменяем путь к папке blockchain
    files = [f for f in os.listdir('blockchain') if f.endswith('.txt')]
    if files:
        print("Список созданных блоков:")
        for file in files:
            print(file)
    else:
        print("Нет созданных блоков.")

if __name__ == "__main__":
    list_blocks()
