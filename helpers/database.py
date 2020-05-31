from pyrogram import Message

from helpers.telegram import handle_username
from models import db, User


def create_user(message: Message):
    """
    Создаем нового юзера в базе данных
    """
    tg_id = message.from_user.id
    username = handle_username(message)

    with db.atomic():
        user = User.create(
            tg_id=tg_id,
            username=username
        )

    return user


def db_save(model):
    """
    Атомарная транзакция сохранения в базе данных
    """
    with db.atomic():
        model.save()
