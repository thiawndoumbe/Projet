# IMPORTATION ET CREATION
import pandas as pd # Pour la manupulation du data frame
import numpy as np # Pour des eventuelles calculs numerique 

# Importation  des donnees
df=pd.read_csv('Hotel Reservations.csv',)
df.head()
# Dimension du data frame
df.shape
#Affichage de la liste des colonne du data frame
df.columns
import sqlite3 # Pour la creation et les manupulations de ma base de donnee
conn = sqlite3.connect('hotel.db')
cursor = conn.cursor()

#Creation de table
cursor.execute('CREATE TABLE hot ( Booking_ID,no_of_adults, no_of_children , no_of_weekend_nights,no_of_week_nights, type_of_meal_plan, required_car_parking_space,room_type_reserved, lead_time, arrival_year, arrival_month,arrival_date, market_segment_type, repeated_guest,no_of_previous_cancellations , no_of_previous_bookings_not_canceled,avg_price_per_room, no_of_special_requests, booking_status)')


# Insersion du data frame dans la base de donnee
from sqlalchemy import create_engine # pour facilliter l'insertion de mon data frame dans ma base donnee

engine = create_engine('sqlite:///hotel.db')
df.to_sql('hot', engine, if_exists='replace', index=False)
# Affichage 
res=cursor.execute('SELECT* FROM hot')
print(res.fetchall())
#Verification des colonnes apres insersion
column_names = [description[0] for description in cursor.description]
print('Column names:', column_names)
# Affichage de la table de ma base de donnee
ht=pd.read_sql("""

SELECT *
   
FROM hot;

""", conn)
ht.head()
# Verification de la dimension de ma table
ht.shape
# ANALYSE DE DONNEES





#1. delais de reservation 


# Les 10 plus longs delais de reservation 
pd.read_sql("""

SELECT*
FROM hot
ORDER BY lead_time DESC
LIMIT 10

""", conn)

# la liste des clients qui reservent sur place
pd.read_sql("""

SELECT*
FROM hot
WHERE lead_time=0 

""", conn)
# Le nombre de clients qui reservent sur place
pd.read_sql("""

SELECT COUNT(*)
FROM hot
WHERE lead_time=0 


""", conn)

#2. Chambres 


# Liste des differents types de chambres a l'hotel
pd.read_sql("""

SELECT DISTINCT room_type_reserved
FROM hot

""", conn)
# Le nombre de reservation par type de chambre (ordre croissant)
pd.read_sql("""

SELECT room_type_reserved, COUNT(room_type_reserved)
FROM hot
GROUP BY room_type_reserved
ORDER BY COUNT(room_type_reserved) DESC


""", conn)


#3.  le nombre de reservation par annee



pd.read_sql("""

SELECT DISTINCT arrival_year , COUNT(arrival_year)
FROM hot
GROUP BY arrival_year
ORDER BY COUNT(arrival_year) ASC

""", conn)


#4. total des revenus par an

pd.read_sql("""

SELECT DISTINCT arrival_year , SUM(avg_price_per_room)
FROM hot
GROUP BY arrival_year
ORDER BY SUM(avg_price_per_room) ASC


""", conn)
# Liste des clients aui sont venus une seule fois 
pd.read_sql("""

SELECT * 
FROM hot
WHERE repeated_guest= '1'

""", conn)
#5.le nombre de clients qui sont venus a l'hotel plus d'une fois (1) et les clients qui sont venus qu'une seule fois(0)
pd.read_sql("""

SELECT DISTINCT repeated_guest , COUNT(repeated_guest)
FROM hot
GROUP BY repeated_guest
ORDER BY COUNT(repeated_guest) ASC

""", conn)
#6.Tranche d'age
# tableau comparatif du nombre de clients adultes et jeunes
pd.read_sql("""

SELECT  SUM(no_of_adults),SUM(no_of_children)
FROM hot

""", conn)
#7.Periode de reservation
# Tableau comparatif du nombre de reservation par weekend et par jours ouvrables
pd.read_sql("""

SELECT  SUM(no_of_weekend_nights),SUM(no_of_week_nights)
FROM hot

""", conn)
#8.Service Restauration
# les plats servis a l'hotel
pd.read_sql("""

SELECT DISTINCT type_of_meal_plan
FROM hot

""", conn)
# Tableau comparatif des types de plat commandes a l'hotel
pd.read_sql("""

SELECT type_of_meal_plan, COUNT(type_of_meal_plan)
FROM hot
GROUP BY type_of_meal_plan
ORDER BY COUNT(type_of_meal_plan) DESC


""", conn)
#9.Date
# Liste des mois par ordre de preference des clients
pd.read_sql("""

SELECT arrival_month, COUNT(arrival_month)
FROM hot
GROUP BY arrival_month	
ORDER BY COUNT(arrival_month)	DESC


""", conn)