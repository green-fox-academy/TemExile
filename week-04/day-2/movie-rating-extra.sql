-- Q1
SELECT distinct b.name
FROM Movie a join Rating c on a.mID = c.mID join Reviewer b on b.rID = c.rID
WHERE a.title = 'Gone with the Wind'
ORDER BY b.name;

-- Q2
SELECT b.name, a.title, c.stars
FROM Movie a join Rating c on a.mID = c.mID join Reviewer b on b.rID = c.rID
WHERE a.director = b.name;

-- Q3
SELECT title as name
FROM Movie
UNION ALL
SELECT name as name
FROM Reviewer
ORDER BY name;

-- Q4
SELECT title
FROM Movie
WHERE title not in (SELECT a.title
              FROM Movie a join Rating c on a.mID = c.mID 
                      join Reviewer b on b.rID = c.rID
              WHERE b.name = 'Chris Jackson');

-- Q7
SELECT a.title, avg(b.stars) as rating
FROM Movie a join Rating b on a.mID = b.mID
GROUP BY a.title
ORDER BY rating DESC, a.title ASC;

-- Q8
SELECT a.name
FROM Reviewer a join Rating b on a.rID = b.rID
GROUP BY b.rID
HAVING count(b.rID) >= 3;