from re import T
import sqlite3 
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()
#VARIABLES
DB_NAME = os.environ.get("DB_NAME")
TABLE_NAME = os.environ.get("TABLE_NAME")
print(TABLE_NAME)
#Local variables
country = "Gabon"
year = 2005

def connect_db(db: str) -> object:

    try:
        con = sqlite3.connect('db.sqlite')
    except Exception as err:
        raise err
    finally:
        cur = con.cursor()

    return cur

cur = connect_db(DB_NAME)

#get rows

#def get_all_rows() -> list:
    #tuples_list = [ row for row in cur.execute('''SELECT * FROM population_years''')]
    
    #return tuples_list

    
#print(get_all_rows())
#print(len(get_all_rows()))

#get all rows with pd

def get_all_rows_pd() -> pd.DataFrame:
    iterable = cur.execute('''SELECT * FROM population_years''')

    return pd.DataFrame(iterable)

df = get_all_rows_pd()
#print(df)

#print(df.columns)

# Rename all the column names
df.columns = ['country', 'population', 'year']
#print(df.columns)
#print(df.head())

# query = '''
# SELECT 
# MAX(population)
# FROM population_years
# WHERE country = "Gabon"
# ''' 

# query = f'''
# SELECT 
# MAX(population)
# FROM population_years
# WHERE country = "{country}"
# ''' 

#print(*cur.execute(query))

#Cerate Max function

def get_max_pop(country: str) -> int:

    query = f'''
    SELECT 
    MAX(population)
    FROM population_years
    WHERE country = "{country}"
    ''' 
    for max in  cur.execute(query):
        return max[0] # return the first elemnt of iterable

country = "Gabon"
print(get_max_pop(country))

#for row in cur.execute(query):
#    print(row)


#print(*df.columns)

def get_min_pop(country: str) -> int:

    query = f'''
    SELECT 
    MIN(population)
    FROM population_years
    WHERE country = "{country}"
    ''' 
    for min in  cur.execute(query):
        return min[0] # return the first elemnt of iterable

country = "Gabon"
#print(get_min_pop(country))

#
def get_pop(func: str, country: str) -> int:

    query = f'''
    SELECT 
    {func}(population)
    FROM population_years
    WHERE country = "{country}"
    ''' 
    for res in  cur.execute(query):
        return res[0]# return the first elemnt of iterable

func = "MIN"      
country = "Gabon"
#print(get_pop(func, country))


query = '''
SELECT year
FROM population_years;
'''

#print(*cur.execute(query))

#print(*df['year'].unique())  

newquery = '''
SELECT country
FROM population_years
WHERE year = '2005'
GROUP BY 1
ORDER BY population ASC
LIMIT 10;
'''

#print(*cur.execute(newquery))

# Extracting the first element in a tupil and putting it in a list using lambda function:


def get_lowest_pop_countries_by_year(year: int) -> list[str]:

    query = f'''
    SELECT country
    FROM population_years
    WHERE year = '{year}'
    GROUP BY 1     
    ORDER BY population ASC
    LIMIT 10;
    '''
    return list(map(lambda x: x[0], cur.execute(query)))
    

print(get_lowest_pop_countries_by_year(year))