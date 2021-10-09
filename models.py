from peewee import *

psql_db = PostgresqlDatabase('hakaton', user = 'postgres')


class BaseModel(Model):
    class Meta:
        database = psql_db


class Users(BaseModel):
    user_id = IntegerField(primary_key = True)
    name = TextField(null = True)
    place = IntegerField(null = True)
    form = IntegerField(null = True)
    link = TextField(null = True)


class Subject(BaseModel):
    sub_id = AutoField()
    title = TextField(unique = True)


class Marks(BaseModel):
    id = AutoField()
    user = ForeignKeyField(Users, column_name = 'user')
    sub = ForeignKeyField(Subject, column_name = 'sub')
    mark = IntegerField(default = -1)


def connect_db():
    psql_db.connect()
    print("БД подключена")


def create_db():
    psql_db.create_tables([Users, Subject, Marks])
    sub = ["Алгебра", "Геометрия", "Информатика",
           "Физика", "Химия",
           "Русский", "Литература"]
    for i in sub:
        Subject.insert(title = i).execute()
    close_db()


def check_user(user_id):
    connect_db()
    temp = Users.get_or_none(user_id)
    close_db()
    return temp


def add(user_data):
    connect_db()
    if Users.get_or_none(user_data["user_id"]):
        Users.update(name = " ".join(user_data["name"]), place = 0, form = 0,
                     link = user_data["call"][0]).where(Users.user_id == user_data["user_id"]).execute()
    else:
        Users.insert(user_id = user_data["user_id"], name = " ".join(user_data["name"]), place = 0, form = 0,
                     link = user_data["call"][0]).on_conflict_ignore().execute()  # plase and form удалить
    for i in user_data["subjects"]:
        sub = Subject.select(Subject.sub_id).where(Subject.title == i[0])
        print(sub[0])
        if Marks.get_or_none((Marks.user == user_data["user_id"]) & (Marks.sub == sub[0])):
            temp = Marks.update({Marks.mark: i[1]}).where((Marks.user == user_data["user_id"]) & (Marks.sub == sub[0]))
            temp.execute()
        else:
            Marks.insert(user = user_data["user_id"], sub = sub[0], mark = i[1]).execute()
    close_db()


def close_db():
    psql_db.close()
    print("БД Отключена")


def main():
    query1 = Marks.select(Users.user_id, Marks.sub, Marks.mark).join_from(Marks, Users).dicts()
    temp = Users.insert(user_id = 123, name = "5654564", place = 0, form = 0)
    temp.execute()
    for i in query1:
        print(i)


if __name__ == "__main__":
    create_db()
