-- this query for lists all shows contained in the database hbtn_0d_tvshows
   -- Each record should display: for tv_shows.title - tv_show_genres.genre_id
   -- for Results must be have sorted in ascending order by tv_shows.title
   -- for and tv_show_genres.genre_id
   -- If this a show doesn’t have a genre, display NULL
   -- This database name will be passed as an argument of the mysql command

SELECT tv_shows.title, tv_show_genres.genre_id FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id=tv_show_genres.show_id
ORDER BY tv_shows.title, tv_show_genres.genre_id;
