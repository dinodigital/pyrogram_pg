from pyrogram import Client
from jobs.sheduler import scheduler
import peeweedbevolve
from models import db

# Инициализация бота
app = Client("Bot")

# Запуск приложения
if __name__ == "__main__":
    # scheduler.start()
    db.evolve(interactive=False, ignore_tables=['basemodel'])
    app.run()
