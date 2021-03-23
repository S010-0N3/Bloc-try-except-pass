import csv

f = open("legislator.csv")
legislator = csv.reader(f)
l = list(legislator)

gender=[]
for row in l:
  gender.append(row[3])

gender = set(gender[1:])


party =[]
for row in l:
  party.append(row[6])

party = set(party[1:])


for row in l:
  if row[6] == "":
    row[6] = "no party"
party =[]

for row in l:
  party.append(row[6])
party = set(party[1:])



for row in l:
  if row[3] == "":
    row[3] = "M"
gender =[]
for row in l:
  gender.append(row[3])
gender = set(gender[1:])

birth_year =[]

for row in l:
  list_row = []
  list_row.append(row[2])
  for x in list_row:
    list_row= x.split("-")
    birth_year.append(list_row[0])
birth_year = set(birth_year)


birth_years2 = []

for row in l:
  birthday = row[2]
  parts = birthday.split("-")
  birth_years2.append(parts[0])

birth_years2 = set(birth_years2)
##################ci dessu VOIR EXERCICE SUR SET######################
#Bloc try/except

# try essaye de convertir la chaine de caractere vide ce qui est impossible mais ne bloque pas la suite du code pour autant.il execute les code apres le except.
try:
  int('')

except Exception:
  print("Impossible de convertir")

#affichage de l'erreur
try:
  int('')

except Exception as exc:
  print(type(exc))
  print(str(exc))

## Pass: meme si il y a une erreur sur le code pass continue le code 
numbers = [1,2,3,4,5,6,7,8,9,10]

for i in numbers:
  try:
    int("")
  except Exception:
    pass

# exercice :
#Mettre en place le block try/except afin de convertir les valeurs de birth_years en entier.

#Assigner le resultat a la liste int_years
int_years = []

for i in birth_year:
  try:
    i =int(i)
    int_years.append(i)
  except Exception as exc:
    print(type(exc))
    print(str(exc))

