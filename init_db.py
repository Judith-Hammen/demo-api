"""
 **************************************
 init_db.py. Initiele setup voor database met users. Het schema staat in schema.sql

 Dit bestand starten: python init_db.py. Doe dit VOORDAT je de webserver gaat gebruiken.

 Behorende bij 'Praktisch Python', door Peter Kassenaar, 2023.
 **************************************
"""

import sqlite3

connection = sqlite3.connect('database.db') # wijzig deze naam als je een andere bestandsnaam wilt.

print('database bestand gemaakt...')

# Open het schema om in te lezen welke rijen, kolommen en data gebruikt wordt.
with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

# Dummy data invoegen
cur.execute("INSERT INTO books (ISBN, title, writer) VALUES (?, ?, ?)",
            ("9789020537963", "de kleur van colorado", "Rebecca Yarros" )
            )

cur.execute("INSERT INTO books (ISBN, title, writer) VALUES (?, ?, ?)",
            ('9789024592470', 'Onverbeterlijk', 'Lisette Jonkman' )
            )

cur.execute("INSERT INTO books (ISBN, title, writer) VALUES (?, ?, ?)",
            ('9783499272134', 'Dochters van een nieuwe tijd', 'Carmen Korn')
            )

cur.execute("INSERT INTO books (ISBN, title, writer) VALUES (?, ?, ?)",
            ('9789025454647', 'Het echte leven', 'Adeline Dieudonné')
            )

# Daadwerkelijk Opslaan in de database en sluiten.
connection.commit()
connection.close()

print('database succesvol opgeslagen.')
