from sqlalchemy import create_engine
from sqlalchemy import text

engine = create_engine('sqlite:///testDB.db')


def simpleExample():
    with engine.connect() as conn:
     result = conn.execute(text('SELECT 2'))
     print(result.all())

simpleExample()