from sqlite3 import connect

data = [
    ("Rise of the Planet of the Apes", 2011, 77),
    ("Dawn of the Planet of the Apes", 2014, 91),
    ("Alien", 1979, 97),
    ("Aliens", 1986, 98),
    ("Mad Max", 1979, 95),
    ("Mad Max 2: The Road Warrior", 1981, 100),
]


def main():
    conn = connect("test.db")
    c = conn.cursor()
    c.execute(
        "CREATE TABLE IF NOT EXISTS MOVIES (id INTEGER PRIMARY KEY, Name TEXT, Year INTEGER, Rating INTEGER)"
    )
    c.executemany("INSERT INTO MOVIES (Name, Year, Rating) VALUES (?, ?, ?)", data)
    conn.commit()
    c.execute("SELECT * FROM MOVIES")
    print(c.fetchone())
    print(c.execute('SELECT name FROM sqlite_master WHERE type = "table" ').fetchall())
    conn.close()


if __name__ == "__main__":
    main()
