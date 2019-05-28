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

-- Q5
SELECT distinct a.name, b.name
FROM Reviewer a, Reviewer b, Movie, Rating c, Rating d
WHERE c.mID = d.mID and 
    c.rID = a.rID and 
    d.rID = b.rID and
    c.rID != d.rID and
    a.name < b.name
 ORDER BY a.name, b.name;

-- Q6
SELECT Reviewer.name, Movie.title, Rating.stars
FROM Reviewer join Rating on Reviewer.rID = Rating.rID
          join Movie on Movie.mID = Rating.mID
WHERE Rating.stars = (SELECT min(Rating.stars) FROM Rating);

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

-- Q9
SELECT a.title, a.director
FROM Movie a, Movie b
WHERE a.title != b.title and 
    a.director = b.director
ORDER BY a.director, a.title;

-- Q10
SELECT Movie.title, avg(Rating.stars) as rate
FROM Movie join Rating on Movie.mID = Rating.mID
GROUP BY Movie.title
Having rate >= (SELECT max(rate) FROM(
                          SELECT avg(stars) as rate
                          FROM Rating
                          GROUP BY mID));

-- Q11
SELECT Movie.title, avg(Rating.stars) as rate
FROM Movie join Rating on Movie.mID = Rating.mID
GROUP BY Movie.title
Having rate <= (SELECT min(rate) FROM(
                          SELECT avg(stars) as rate
                          FROM Rating
                          GROUP BY mID));

-- Q12
SELECT a.director, Movie.title, a.rate
FROM (SELECT Movie.director, max(Rating.stars) as rate, Movie.mID
    FROM Movie join Rating on Movie.mID = Rating.mID
    WHERE Movie.director is not NULL
    GROUP BY Movie.director
    ) as a, Movie
WHERE a.mID = Movie.mID;