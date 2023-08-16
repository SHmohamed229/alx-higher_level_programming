-- this query for lists all genres of the show Dexter.
   -- this Each for record should Display:
      -- tv_genres.name
   -- for Result must be have sorted in ascending order by the genre name
   -- This Database name will be passed as an argument of the mysql command

SELECT name FROM tv_genres
JOIN tv_show_genres ON id=tv_show_genres.genre_id
JOIN tv_shows ON tv_shows.id=tv_show_genres.show_id
WHERE tv_shows.title = 'Dexter'
ORDER BY name;
