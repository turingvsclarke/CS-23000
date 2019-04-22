import sqlite3
from Enigma import*
import pdb

# We're going to connect to the enigmas database and test some

enigmaDB = sqlite3.connect("enigmas.db")

# This sets the cursur so that it will select individual items within a row
enigmaDB.row_factory = sqlite3.Row
c = enigmaDB.cursor()

# Let's now try to get a list of all the ids of all the machines and how many rotors they have

result = c.execute("SELECT * FROM enigmas")
ids = []
names = []
sizes = []
for x in result:
    ids.append(x['id'])
    names.append(x['name'])
# Find out how many rotors there are for each machine
for x in ids:
    result = c.execute("SELECT * FROM enigma_rotors WHERE enigma_id = ?",(x,))
    size = 0
    for y in result:
        size+=1
    sizes.append(size)
print(ids,names,sizes)
enigmaDB.commit()

