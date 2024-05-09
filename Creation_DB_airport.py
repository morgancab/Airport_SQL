import pandas as pd
import sqlite3
#!pip install ipython-sql

airport= pd.read_csv('Data/airports.csv')
flights= pd.read_csv('Data/flights.csv')
airlines= pd.read_csv('Data/airlines.csv')

#Ytb video : https://www.youtube.com/watch?v=sDY_fKe_JVw&t=154s
cnn = sqlite3.connect('jupyter_sql_tutorial.db')

airport.to_sql('airport', cnn)
flights.to_sql('flights', cnn)
airlines.to_sql('airlines', cnn)


