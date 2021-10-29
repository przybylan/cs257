# Author: Nate Przybyla
import sys
import argparse
import flask
import json
import psycopg2
from config import database
from config import user

app = flask.Flask(__name__)

@app.route('/games')
def get_games():
    try:
        connection = psycopg2.connect(database=database, user=user)
    except Exception as e:
        print(e)
        exit()
    try:
        cursor = connection.cursor()
        query = 'SELECT games.id, games.year, games.season, games.city FROM games ORDER BY games.year'
        cursor.execute(query)
    except Exception as e:
        print(e)
        exit()
    games_list = []
    for row in cursor:
        games = {}
        games['id'] = row[0]
        games['year'] = row[1]
        games['season'] = row[2]
        games['city'] = row[3]
        games_list.append(games)
    connection.close()
    return json.dumps(games_list)

@app.route('/nocs')
def get_nocs():
    try:
        connection = psycopg2.connect(database=database, user=user, password=password)
    except Exception as e:
        print(e)
        exit()
    try:
        cursor = connection.cursor()
        query = 'SELECT nocs.abbreviation, nocs.name FROM nocs ORDER BY nocs.abbreviation'
        cursor.execute(query)
    except Exception as e:
        print(e)
        exit()
    nocs_list = []
    for row in cursor:
        noc = {}
        noc['abbreviation'] = row[0]
        noc['name'] = row[1]
        nocs_list.append(noc)
    connection.close()
    return json.dumps(nocs_list)

@app.route('/medalists/games/<games_id>')
def medalists_by_games(games_id):
    try:
        connection = psycopg2.connect(database=database, user=user, password=password)
    except Exception as e:
        print(e)
        exit()
    noc = flask.request.args.get('noc')
    if noc is not None: 
        query = ''' SELECT athletes.id, athletes.name, results.athlete_sex, results.sport, events.name, results.medal
                FROM athletes, results, events, nocs
                WHERE athletes.id = results.athlete_id
                AND events.id = results.event_id
                AND nocs.id = results.noc_id
                AND results.medal <> %s
                AND results.games_id = %s
                AND nocs.abbreviation = %s '''
        try:
            cursor = connection.cursor()
            cursor.execute(query, ('NA', games_id, noc,))
        except Exception as e:
            print(e)
            exit()
    else:
        query = ''' SELECT athletes.id, athletes.name, results.athlete_sex, results.sport, events.name, results.medal
                FROM athletes, results, events
                WHERE athletes.id = results.athlete_id
                AND events.id = results.event_id
                AND results.medal <> %s
                AND results.games_id = %s '''
        try:
            cursor = connection.cursor()
            cursor.execute(query, ('NA', games_id,))
        except Exception as e:
            print(e)
            exit()
    medalists_list = []
    for row in cursor:
        medalist = {}
        medalist['athlete_id'] = row[0]
        medalist['athlete_name'] = row[1]
        medalist['athlete_sex'] = row[2]
        medalist['sport'] = row[3]
        medalist['event'] = row[4]
        medalist['medal'] = row[5]
        medalists_list.append(medalist)
    connection.close()
    return json.dumps(medalists_list)

if __name__ == '__main__':
    parser = argparse.ArgumentParser('A Flask application using the olympics database')
    parser.add_argument('host', help='the host on which this application is running')
    parser.add_argument('port', type=int, help='the port on which this application is listening')
    arguments = parser.parse_args()
    app.run(host=arguments.host, port=arguments.port, debug=True)