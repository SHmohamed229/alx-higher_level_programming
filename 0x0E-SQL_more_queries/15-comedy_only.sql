-- this query for lists all Comedy show in the database hbtn_0d_tvshows
-- Display the num of show linked to each
   -- Each record should be Display:
      -- tv_shows.title
   -- for Result must be have a sorted in ascending order by the show title
   -- This Database name will be passed as an argument of the mysql command

SELECT title FROM tv_shows
JOIN tv_show_genres ON id=tv_show_genres.show_id
JOIN tv_genres ON tv_genres.id=tv_show_genres.genre_id
WHERE tv_genres.name = 'Comedy'
ORDER BY title;
