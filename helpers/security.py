from cryptography.fernet import Fernet
from config import get_cfg

key = str.encode(get_cfg('security')['key'])


def generate_key():
    """
    Генерирует секретный ключ
    """
    return Fernet.generate_key()


def enc(data):
    """
    Шифрует строку при помощи ключа
    """
    return Fernet(key).encrypt(data.encode('UTF-8')).decode('UTF-8')


def dec(data):
    """
    Расшифровывает строку
    """
    return Fernet(key).decrypt(data.encode('UTF-8')).decode('UTF-8')
