import peewee
from decouple import config

db = peewee.PostgresqlDatabase(config('DB_NAME'), host=config('HOST'),
                               port=config('PORT'), user=config("USER"),
                               password=config("PASSWORD"))


class Dep(peewee.Model):
    name = peewee.CharField(max_length=50)
    part = peewee.TextField()
    # year = peewee.IntegerField()
    # link = peewee.TextField()
    image = peewee.TextField()
    # price_usd = peewee.IntegerField()

    class Meta:
        database = db
        db_table = 'deps'


db.create_tables([Dep])
