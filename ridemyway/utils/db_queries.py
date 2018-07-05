"""
    DATABASE QUERIES
"""

from flask import current_app as app
import psycopg2
import psycopg2.extras


def insert_user(user):
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
        app.conn.rollback()


def select_user(username=None, email=None):
    cur = app.conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    search_by_username_email_sql = """
    SELECT * FROM appuser WHERE username=%s OR email=%s;
    """
    cur.execute(search_by_username_email_sql, (username, email))
    user = cur.fetchone()
    app.conn.commit()
    cur.close()
    if user:
        return user


def update_user(user_details):
    pass
