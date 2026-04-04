from sqlalchemy import create_engine, text

engine = create_engine('sqlite:///sqlDB.db', echo=True)

# object use to execute commands
conn = engine.connect()

conn.execute(text("CREATE TABLE IF NOT EXISTS Employees (id INTEGER, name TEXT, age INTEGER)"))
conn.commit()


from sqlalchemy.orm import Session

session = Session(engine)

session.execute(text("""INSERT INTO Employees (id, name, age)
                        VALUES(1, "Mike", 25),
                              (2, "Johnson", 45),
                              (3, "Mina", 23);
                     """))

session.commit()

