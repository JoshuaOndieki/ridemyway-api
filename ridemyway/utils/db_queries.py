"""
    DATABASE QUERIES
"""

from flask import current_app as app


def sql_signup(user):
    sql = """INSERT INTO
                appuser  (username, name, gender, usertype, date_joined,
                contacts, email, password)
                VALUES ('%s','%s','%s','%s', '%s', %d, '%s', '%s')""" % (
                    user.username,
                    user.name,
                    user.gender,
                    user.usertype,
                    user.date_joined,
                    user.contacts,
                    user.email,
                    user.password)
    cur = app.conn.cursor()
    try:
        cur.execute(sql)
        app.conn.commit()
        return True
    except Exception:
        app.conn.rollback


def get_user(username=None, email=None):
    cur = app.conn.cursor()
    search_by_username_email_sql = """
    SELECT * FROM appuser WHERE username=%s OR email=%s;
    """ % (username, email)
    cur.execute(search_by_username_email_sql)
    exists = cur.fetchone()

    if exists:
        return True
