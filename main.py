import sqlite3

connection = sqlite3.connect('AnimalKingdom.db')
cursor = connection.cursor()

cursor.execute('DROP TABLE IF EXISTS Animals')
cursor.execute('''
CREATE TABLE Animals (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Name TEXT NOT NULL,
    Type TEXT NOT NULL
)
''')

animals_data = [
    ("Лев", "Ссавець"),
    ("Крокодил", "Плазун"),
    ("Орел", "Птах"),
    ("Морська черепаха", "Плазун"),
    ("Мавпа", "Ссавець")
]
cursor.executemany('INSERT INTO Animals (Name, Type) VALUES (?, ?)', animals_data)
connection.commit()

cursor.execute("UPDATE Animals SET Name = 'Сокіл' WHERE Name = 'Орел'")
connection.commit()

print("1. Тільки ссавці")
cursor.execute("SELECT * FROM Animals WHERE Type = 'Ссавець'")
mammals = cursor.fetchall()
for animal in mammals:
    print(animal)

print("\n2. Всі звірі в базі")
cursor.execute("SELECT * FROM Animals")
all_records = cursor.fetchall()
for record in all_records:
    print(record)

connection.close()
print("\nВсі дані збережені")


