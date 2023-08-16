-- this query for lists all shows contained in hbtn_0d_tvshows without a genre linked
   -- Each record should display: for tv_shows.title - tv_show_genres.genre_id
   -- for Results must be have sorted in ascending order by tv_shows.title
   -- also and tv_show_genres.genre_id
   -- This database name will be passed as an argument of the mysql command

SELECT title, tv_show_genres.genre_id FROM tv_shows
LEFT JOIN tv_show_genres ON id=tv_show_genres.show_id
WHERE tv_show_genres.show_id IS NULL
ORDER BY title, tv_show_genres.genre_id;
