import sqlite3 as sq

def create_db():
    try:
        sqlite_connection = sq.connect('log.db')
        cursor = sqlite_connection.cursor()
        print("База данных создана и успешно подключена к sqLite")

        sqlite_select_query = "select sqlite_version();"
        cursor.execute(sqlite_select_query)
        record = cursor.fetchall()
        print("Версия базы данных sqLite: ", record)
        cursor.close()

    except sq.Error as error:
        print("Ошибка при подключении к sqlite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с sqLite закрыто")


def create_table():
    sqlite_connection = sq.connect('log.db')
    sqlite_create_table_query = ('CREATE TABLE sqlitedb_developers (\n'
                                 '                                userid varchar,\n'
                                 '                                username varchar,\n'
                                 '                                goods varchar,\n'
                                 '                                color varchar,\n'
                                 '                                size varchar,\n'
                                 '                                photo varchar,\n'
                                 '                                comment varchar,\n'
                                 '                                type varchar,\n'
                                 '                                contact varchar);')

    cursor = sqlite_connection.cursor()
    print("База данных подключена к sqLite")
    cursor.execute(sqlite_create_table_query)
    sqlite_connection.commit()
    print("Таблица sqLite создана")

    cursor.close()


def insert_id(userid):
    sqlite_connection = sq.connect('log.db')
    sqlite_create_table_query = ('insert into sqlitedb_developers(userid) select ' + str(userid) + ' as userid;')

    cursor = sqlite_connection.cursor()
    cursor.execute(sqlite_create_table_query)
    sqlite_connection.commit()
    print('id inserted')
    cursor.close()


def insert_name(userid, name):
    sqlite_connection = sq.connect('log.db')
    sqlite_create_table_query = (
            'update sqlitedb_developers set username = \'' + str(name) + '\' where userid = ' + str(userid) + ';')

    cursor = sqlite_connection.cursor()
    cursor.execute(sqlite_create_table_query)
    sqlite_connection.commit()
    cursor.close()


def insert_goods(userid, goods):
    sqlite_connection = sq.connect('log.db')
    sqlite_create_table_query = (
                'update sqlitedb_developers set goods = \'' + str(goods) + '\' where userid = ' + str(userid) + ';')

    cursor = sqlite_connection.cursor()
    cursor.execute(sqlite_create_table_query)
    sqlite_connection.commit()
    print('goods inserted')
    cursor.close()


def insert_color(userid, color):
    sqlite_connection = sq.connect('log.db')
    sqlite_create_table_query = (
                'update sqlitedb_developers set color = \'' + str(color) + '\' where userid = ' + str(userid) + ';')

    cursor = sqlite_connection.cursor()
    cursor.execute(sqlite_create_table_query)
    sqlite_connection.commit()
    cursor.close()


def insert_size(userid, size):
    sqlite_connection = sq.connect('log.db')
    sqlite_create_table_query = (
                'update sqlitedb_developers set size = \'' + str(size) + '\' where userid = ' + str(userid) + ';')

    cursor = sqlite_connection.cursor()
    cursor.execute(sqlite_create_table_query)
    sqlite_connection.commit()
    cursor.close()


def insert_photo(userid, photo):
    sqlite_connection = sq.connect('log.db')
    sqlite_create_table_query = (
                'update sqlitedb_developers set photo = \'' + str(photo) + '\' where userid = ' + str(userid) + ';')

    cursor = sqlite_connection.cursor()
    cursor.execute(sqlite_create_table_query)
    sqlite_connection.commit()
    cursor.close()


def insert_comment(userid, comment):
    sqlite_connection = sq.connect('log.db')
    sqlite_create_table_query = (
                'update sqlitedb_developers set comment = \'' + str(comment) + '\' where userid = ' + str(userid) + ';')

    cursor = sqlite_connection.cursor()
    cursor.execute(sqlite_create_table_query)
    sqlite_connection.commit()
    cursor.close()


def insert_type(userid, type):
    sqlite_connection = sq.connect('log.db')
    sqlite_create_table_query = (
                'update sqlitedb_developers set type = \'' + str(type) + '\' where userid = ' + str(userid) + ';')

    cursor = sqlite_connection.cursor()
    cursor.execute(sqlite_create_table_query)
    sqlite_connection.commit()
    cursor.close()


def get_row(userid):
    records = []
    sqlite_connection = sq.connect('log.db')
    sqlite_create_table_query = 'select * from sqlitedb_developers where userid = ' + str(userid) + ';'

    cursor = sqlite_connection.cursor()
    cursor.execute(sqlite_create_table_query)
    records = cursor.fetchall()

    sqlite_connection.commit()
    cursor.close()
    return records


def insert_contact(userid, contact):
    sqlite_connection = sq.connect('log.db')
    sqlite_create_table_query = (
                'update sqlitedb_developers set contact = \'' + str(contact) + '\' where userid = ' + str(userid) + ';')

    cursor = sqlite_connection.cursor()
    cursor.execute(sqlite_create_table_query)
    sqlite_connection.commit()
    cursor.close()


def truncate():
    sqlite_connection = sq.connect('log.db')
    sqlite_create_table_query = (
                'delete from sqlitedb_developers;')

    cursor = sqlite_connection.cursor()
    cursor.execute(sqlite_create_table_query)
    sqlite_connection.commit()
    cursor.close()


def delete_id(userid):
    sqlite_connection = sq.connect('log.db')
    cursor = sqlite_connection.cursor()
    sqlite_create_table_query = 'delete from sqlitedb_developers where userid = ' + str(userid) + ';'
    cursor.execute(sqlite_create_table_query)
    sqlite_connection.commit()
    cursor.close()


