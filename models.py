from peewee import Model, CharField, IntegerField, DateTimeField, PostgresqlDatabase, TextField
from playhouse.postgres_ext import JSONField

from datetime import datetime

from config import get_cfg

db_cfg = get_cfg('db')
db_conn = {
    'host': db_cfg['host'],
    'user': db_cfg['user'],
    'password': db_cfg['password'],
    'database': db_cfg['database'],
    'autorollback': db_cfg['autorollback']
}
db = PostgresqlDatabase(**db_conn)


msg_ids = {
    "b_info": 0,
    "b_main": 0
}


class BaseModel(Model):
    class Meta:
        database = db


class User(BaseModel):
    tg_id = IntegerField()
    username = CharField()
    registered = DateTimeField(default=datetime.now)


class Msg(BaseModel):
    tg_id = IntegerField()
    text = TextField()
    date = DateTimeField(default=datetime.now)
