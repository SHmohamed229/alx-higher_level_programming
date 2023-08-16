-- this query for lists all genres contained in hbtn_0d_ and the num of shows linked to each
   -- this Each for record should Display:
      -- [[TV Showing genre]] - [Num of shows linked to this genre]
   -- for Results must have be sorted in order by the number of shows linkeda
   -- This  database name will be passed as an argument of the mysql command

SELECT name AS genre, COUNT(*) AS number_of_shows FROM tv_genres
JOIN tv_show_genres ON id=tv_show_genres.genre_id
GROUP BY tv_show_genres.genre_id
ORDER BY number_of_shows DESC;
