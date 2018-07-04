"""
    DATABASE QUERIES
"""

from flask import current_app as app
import psycopg2


def sql_signup(user):
    sql = "INSERT INTO appuser  (username, name, gender, usertype, date_joined, contacts, email, password) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    data = (
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
        cur.execute(sql, data)
        app.conn.commit()
        return True
    except psycopg2.Error:
        print('Roll back, user not added')
        app.conn.rollback()
        return 0


def get_user(username=None, email=None):
    cur = app.conn.cursor()
    search_by_username_email_sql = """
    SELECT * FROM appuser WHERE username=%s OR email=%s;
    """
    cur.execute(search_by_username_email_sql, (username, email))
    exists = cur.fetchone()
    app.conn.commit()
    cur.close()

    if exists:
        return True
