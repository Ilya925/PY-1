import sqlite3

conn = sqlite3.connect('test.db')
cursor = conn.cursor()


"""
DDL - Создание таблиц
DML - Заполнение, корректировка значений.....
SELECT - получение данных
"""

cursor.execute("""CREATE TABLE IF NOT EXISTS car
(id INTEGER PRIMARY KEY NOT NULL,
name TEXT)""")
# cursor.execute("INSERT INTO car (name) VALUES (?)", ('Москвич',))
# conn.commit()
result = cursor.execute("SELECT * FROM car")
# print(result.fetchall())
for row, n in result:
    print(f'Id: {row}, Name: {n}')
"""
SELECT * FROM car;
SELECT name, year FROM car;
SELECT name, year FROM car WHERE year > 2000;
ALTER TABLE car ADD COLUMN type; 
ALTER TABLE car RENAME COLUMN type TO energy; 
INSERT INTO car (name, energy) VALUES('Toyota', 'diesel');
SELECT name, year FROM car WHERE year BETWEEN 2004 AND 2026 ;

SELECT name, year FROM car WHERE name in ('Mercedes', 'LADA');
SELECT name, year FROM car WHERE year LIKE '202_' ;
SELECT name, year FROM car WHERE year LIKE '20%'  AND name = 'Toyota';
SELECT DISTINCT name FROM car ;
SELECT name, year FROM car ORDER BY name DESC, year DESC;
SELECT * FROM (SELECT * FROM persone WHERE name = 'Piter') as nmn JOIN car ON nmn.id = car.persone_id
SELECT name, MAX(cnt) FROM car
SELECT name, year FROM car ORDER BY name DESC, year DESC LIMIT 1, 3
"""