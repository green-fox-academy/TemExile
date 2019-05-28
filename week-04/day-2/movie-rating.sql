-- Q1
SELECT title
FROM Movie
WHERE director = 'Steven Spielberg';

-- Q2
SELECT distinct a.year
FROM Movie a join Rating b on a.mID = b.mID
WHERE b.stars >= 4
ORDER BY a.year ASC;

-- Q3
SELECT a.title
FROM Movie a left join Rating b on a.mID = b.mID
WHERE b.stars is NULL;

-- Q4
SELECT a.name
FROM Reviewer a join Rating b on a.rID = b.rID
WHERE b.ratingDate is NULL;

-- Q5
SELECT b.name, a.title, c.stars, c.ratingDate
FROM Movie a join Rating c on a.mID = c.mID join Reviewer b on b.rID = c.rID
ORDER BY b.name, a.title, c.stars;