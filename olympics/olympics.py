'''
    olympics.py
    Nate Przybyla
'''
import psycopg2
import sys

from config import password
from config import database
from config import user

# Prints all athletes from selected NOC
def get_athletes_by_noc(noc): 
    try:
        connection = psycopg2.connect(database=database, user=user, password=password)
    except Exception as e:
        print(e)
        exit()
    try:
        cursor = connection.cursor()
        query = '''SELECT DISTINCT athletes.name
                FROM athletes, nocs, results
                WHERE nocs.abbreviation = %s
                AND athletes.id = results.athlete_id
                AND nocs.id = results.noc_id;'''
        cursor.execute(query, (noc,))
    except Exception as e:
        print(e)
        exit()

    for row in cursor:
        print(row[0])

    connection.close

# Prints all NOCS that have won a gold medal, ordered by decreasing amount of golds
def get_nocs_by_medal():
    try:
        connection = psycopg2.connect(database=database, user=user, password=password)
    except Exception as e:
        print(e)
        exit()
    try:
        cursor = connection.cursor()
        query = '''SELECT nocs.name, COUNT(results.medal)
                FROM nocs, results
                WHERE nocs.id = results.noc_id
                AND results.medal = 'Gold'
                GROUP BY nocs.name
                ORDER BY COUNT(results.medal) DESC;'''
        cursor.execute(query)
    except Exception as e:
        print(e)
        exit()

    for row in cursor:
        print('NOC:', row[0] + '; Gold Medals:', row[1])

    connection.close

# Prints the events that took place in a specific games
def get_events_by_games(season, year):
    try:
        connection = psycopg2.connect(database=database, user=user, password=password)
    except Exception as e:
        print(e)
        exit()
    try:
        cursor = connection.cursor()
        query = '''SELECT DISTINCT events.name
                FROM games, events, results
                WHERE games.season = %s
                AND games.year = %s
                AND events.id = results.event_id
                AND games.id = results.games_id;'''
        cursor.execute(query, (season, year,))
    except Exception as e:
        print(e)
        exit()

    for row in cursor:
        print('Events:', row[0])

    connection.close

# Command line stuff
def main():
    if sys.argv[1] == '-h' or sys.argv[1] == '--help':
        print('''Command Line Options:
        List NOCs by Gold Medals: python3 olympics.py nocs_by_golds
        List Athletes by NOC: python3 olympics.py athletes_by_noc [NOC Abbreviation]
        List Events by Games: python3 olympics.py events_by_games [Games Season] [Games Year]''')
    elif sys.argv[1] == 'nocs_by_golds':
        get_nocs_by_medal()
    elif sys.argv[1] == 'athletes_by_noc':
        get_athletes_by_noc(sys.argv[2])
    elif sys.argv[1] == 'events_by_games':
        get_events_by_games(sys.argv[2], sys.argv[3])


if __name__ == '__main__':
    main()


