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
        Subject.insert(title = i).on_conflict_ignore().execute()
    close_db()


def check_user(user_id):
    connect_db()
    temp = Users.get_or_none(user_id)
    close_db()
    return temp


def add(user_data):
    connect_db()
    user_data['place_of_study'] = 1 if user_data['place_of_study'] == 'Университет' else 0
    if Users.get_or_none(user_data["user_id"]):
        Users.update(name = " ".join(user_data["name"]), place = user_data['place_of_study'], form = user_data['level_of_study'],
                     link = user_data["call"]).where(Users.user_id == user_data["user_id"]).execute()
    else:
        Users.insert(user_id = user_data["user_id"], name = " ".join(user_data["name"]), place = user_data['place_of_study'], form = user_data['level_of_study'],
                     link = user_data["call"]).on_conflict_ignore().execute()
    for i in user_data["subjects"]:
        sub = Subject.select(Subject.sub_id).where(Subject.title == i[0])
        print(sub[0])
        if Marks.get_or_none((Marks.user == user_data["user_id"]) & (Marks.sub == sub[0])):
            temp = Marks.update({Marks.mark: i[1]}).where((Marks.user == user_data["user_id"]) & (Marks.sub == sub[0]))
            temp.execute()
        else:
            Marks.insert(user = user_data["user_id"], sub = sub[0], mark = i[1]).execute()
    close_db()


def find_person(user_id):
    connect_db()
    trouble = Marks.select(Marks.sub).where((Marks.user == user_id) & (Marks.mark < 7))
    qq = Marks.select(Marks.user, fn.COUNT(Marks.sub), fn.SUM(Marks.mark)).where(
        (Marks.user != user_id) & (Marks.mark > 6) & (Marks.sub.in_(trouble))).group_by(Marks.user).order_by(
        -fn.COUNT(Marks.sub), -fn.SUM(Marks.mark))
    qq = qq.dicts()
    res = Users.select(Users.name, Users.link).where(qq[0]['user']).dicts()
    close_db()
    return res


def close_db():
    psql_db.close()
    print("БД Отключена")


def main():
    trouble = Marks.select(Marks.sub).where((Marks.user == '611120147') & (Marks.mark < 7))
    people = []
    qq = Marks.select().where((Marks.user != '611120147') & (Marks.mark > 6) & (Marks.sub.in_(trouble)))
    for i in qq:
        print(i)


if __name__ == "__main__":
    create_db()
