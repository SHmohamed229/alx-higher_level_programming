-- This Query for lists all shows in hbtn_0d_tvshows that have at least one genre linked
   -- Each record should display: for tv_shows.title - tv_show_genres.genre_id
   -- for Results must have be sorted in ascending order by tv_shows.title
   -- this for and tv_show_genres.genre_id
   -- This database name will be passed as an argument of the mysql command

SELECT tv_shows.title, tv_show_genres.genre_id FROM tv_shows
JOIN tv_show_genres ON tv_shows.id=tv_show_genres.show_id
ORDER BY tv_shows.title, tv_show_genres.genre_id;
