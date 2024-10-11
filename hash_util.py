import hashlib

def hash_data(data):
    """Функция для хеширования данных блока."""
    return hashlib.sha256(data.encode()).hexdigest()
