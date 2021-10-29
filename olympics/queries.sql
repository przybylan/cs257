SELECT nocs.name, nocs.abbreviation
FROM nocs
ORDER BY nocs.abbreviation;

SELECT athletes.name, nocs.name
FROM athletes, nocs, results
WHERE athletes.id = results.athlete_id
AND nocs.id = results.noc_id
AND nocs.name = 'Kenya';

SELECT results.medal, games.year
FROM athletes, games, results
WHERE athletes.id = results.athlete_id
AND games.id = results.games_id
AND athletes.name LIKE '%Louganis%'
AND results.medal <> 'NA'
ORDER BY games.year;

SELECT nocs.name, COUNT(results.medal)
FROM nocs, results
WHERE nocs.id = results.noc_id
AND results.medal <> 'NA'
GROUP BY nocs.name
ORDER BY COUNT(results.medal) DESC;