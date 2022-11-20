import sqlite3 as sq


def sql_start():
    global d_base, cur
    d_base = sq.connect('users_requests.db')
    cur = d_base.cursor()
    if d_base:
        print('База данных подключена успешно')
    cur.execute('CREATE TABLE IF NOT EXISTS users_requests(request_id INTEGER PRIMARY KEY AUTOINCREMENT, '
                'user_id INTEGER, requests TEXT)')
    d_base.commit()


def sql_add_request(user, request):
    cur.execute(f'INSERT INTO users_requests(user_id, requests) VALUES(\'{user}\', \'{request}\')')
    d_base.commit()
