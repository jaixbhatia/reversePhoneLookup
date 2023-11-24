import sqlite3
import json

def create_connection(db_file):
    """ Create a database connection to the SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except sqlite3.Error as e:
        print("SQLite error:", e)
    return conn

def create_table(conn):
    """ Create a table if it doesn't exist """
    create_table_sql = ''' CREATE TABLE IF NOT EXISTS cache (
                                        phone_number text PRIMARY KEY,
                                        names text
                                    ); '''
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except sqlite3.Error as e:
        print("SQLite error:", e)

def add_to_cache(conn, phone_number, names):
    """ Add a new entry to the cache """
    sql = ''' INSERT OR REPLACE INTO cache(phone_number, names)
              VALUES(?, ?) '''
    cur = conn.cursor()
    try:
        # Serialize the names list to JSON format before inserting it
        serialized_names = json.dumps(names)
        cur.execute(sql, (phone_number, serialized_names))
        conn.commit()
    except sqlite3.Error as e:
        print("SQLite error:", e)


def get_from_cache(conn, phone_number):
    """ Query names by phone_number """
    cur = conn.cursor()
    cur.execute("SELECT names FROM cache WHERE phone_number=?", (phone_number,))

    row = cur.fetchone()  # Use fetchone to get a single result

    if row:
        return row[0]  # Return the JSON string
    else:
        return None
