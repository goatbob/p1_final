"""
program: connect_to_database.py
author: kyle godwin
last date modified: 18 april 2023

Connect to database, create tables, return rows
"""
import sqlite3
from sqlite3 import Error


def create_connection(db):
    """ Connect to a SQLite database
    :param db: filename of database
    :return connection if no error, otherwise None"""
    try:
        conn = sqlite3.connect(db)
        return conn
    except Error as err:
        print(err)
    return None


def create_table(conn, sql_create_table):
    """ Creates table with give sql statement
    :param conn: Connection object
    :param sql_create_table: a SQL CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(sql_create_table)
    except Error as e:
        print(e)


def create_database(database):

    sql_create_incident_table = """ CREATE TABLE IF NOT EXISTS incident (
                                        id integer PRIMARY KEY,
                                        date text NOT NULL,
                                        time text NOT NULL,
                                        employee text NOT NULL,
                                        incidenttype text NOT NULL,
                                        incidentdescription text NOT NULL
                                    ); """

    conn = create_connection(database)
    if conn is not None:
        create_table(conn, sql_create_incident_table)
    else:
        print("Unable to connect to " + str(database))


def create_incident(conn, incident):
    """Create a new person for table
    :param conn:
    :param incident:
    :return: person id
    """
    sql = ''' INSERT INTO incident(date, time, employee, incidenttype, incidentdescription)
              VALUES(?,?,?,?,?) '''
    cur = conn.cursor()  # cursor object
    cur.execute(sql, incident)
    return cur.lastrowid  # returns the row id of the cursor object, the person id


def select_all_incidents(conn):
    """Query all rows of incident table
    :param conn: the connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM incident")

    rows = cur.fetchall()

    return rows  # return the rows
