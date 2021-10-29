'''
    convert.py
    Nate Przyla
    Adapted from code written by Jeff Ondich
'''
import csv

# (1) Create a dictionary that maps athlete_id -> athlete_name
#       and then save the results in athletes.csv
athletes = {}
original_data_file = open('athlete_events.csv')
reader = csv.reader(original_data_file)
athletes_file = open('athletes.csv', 'w')
writer = csv.writer(athletes_file)
heading_row = next(reader) # eat up and ignore the heading row of the data file
for row in reader:
    athlete_id = row[0]
    athlete_name = row[1]
    if athlete_id not in athletes:
        athletes[athlete_id] = athlete_name
        writer.writerow([athlete_id, athlete_name])
athletes_file.close()
original_data_file.close()

# (2) Create a dictionary that maps event_name -> event_id
#       and then save the results in events.csv
events = {}
original_data_file = open('athlete_events.csv')
reader = csv.reader(original_data_file)
events_file = open('events.csv', 'w')
writer = csv.writer(events_file)
heading_row = next(reader) # eat up and ignore the heading row of the data file
for row in reader:
    event_name = row[13]
    if event_name not in events:
        event_id = len(events) + 1
        events[event_name] = event_id
        writer.writerow([event_id, event_name])
events_file.close()
original_data_file.close()

games = {}
original_data_file = open('athlete_events.csv')
reader = csv.reader(original_data_file)
games_file = open('games.csv', 'w')
writer = csv.writer(games_file)
heading_row = next(reader)
for row in reader:
    games_name = row[8]
    games_year = row[9]
    games_season = row[10]
    games_city = row[11]
    if games_name not in games:
        games_id = len(games) + 1
        games[games_name] = games_id
        writer.writerow([games_id, games_year, games_season, games_city])
games_file.close()
original_data_file.close()

nocs = {}
original_data_file2 = open('noc_regions.csv')
reader2 = csv.reader(original_data_file2)
nocs_file = open('nocs.csv', 'w')
writer = csv.writer(nocs_file)
heading_row = next(reader2)
for row in reader2:
    noc_name = row[1]
    noc_abbreviation = row[0]
    noc_id = len(nocs) + 1
    nocs[noc_abbreviation] = noc_id
    writer.writerow([noc_id, noc_name, noc_abbreviation])
nocs_file.close()

# (3) For each row in the original athlete_events.csv file, build a row
#       for our new event_results.csv table
original_data_file = open('athlete_events.csv')
reader = csv.reader(original_data_file)
event_results_file = open('results.csv', 'w')
writer = csv.writer(event_results_file)
heading_row = next(reader) # eat up and ignore the heading row of the data file
for row in reader:
    athlete_id = row[0]     
    event_name = row[13]
    event_id = events[event_name] # this is guaranteed to work by section (2)
    games_name = row[8]
    games_id = games[games_name]
    noc_abbreviation = row[7]
    noc_id = nocs[noc_abbreviation]
    athlete_sex = row[2]
    sport = row[12]
    medal = row[14]
    writer.writerow([athlete_id, event_id, noc_id, games_id, athlete_sex, sport, medal])
event_results_file.close()
original_data_file.close()
