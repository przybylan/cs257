CREATE TABLE nocs (
	id INTEGER,
	name TEXT,
	abbreviation TEXT
);

CREATE TABLE athletes (
	id INTEGER,
	name TEXT
);

CREATE TABLE events (
	id INTEGER,
	name TEXT
);

CREATE TABLE games (
	id INTEGER,
	year INTEGER,
	season TEXT,
	city TEXT
);

CREATE TABLE results (
	athlete_id INTEGER,
	event_id INTEGER,
	noc_id INTEGER,
	games_id INTEGER,
	athlete_sex TEXT,
	sport TEXT,
	medal TEXT
);
