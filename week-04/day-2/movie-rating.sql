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

-- Q6
SELECT Reviewer.name, Movie.title
FROM Rating a, Rating b, Reviewer, Movie
WHERE a.rID = b.rID and
    a.mID = b.mID and
    Reviewer.rID = b.rID and
    Movie.mID = b.mID and
    a.ratingDate < b.ratingDate and
    a.stars < b.stars;

-- Q7
SELECT a.title as title, b.stars as stars
FROM Movie a join Rating b on a.mID = b.mID
GROUP BY a.title
Having stars = max(b.stars)
ORDER BY title;

-- Q8
SELECT a.title as Title, a.stars - b.stars as spread
FROM (SELECT Movie.title, max(Rating.stars) as stars
    FROM Movie join Rating on Movie.mID = Rating.mID
    GROUP BY Movie.title) as a
    join
    (SELECT Movie.title, min(Rating.stars) as stars
    FROM Movie join Rating on Movie.mID = Rating.mID
    GROUP BY Movie.title) as b
    on a.title = b.title
ORDER BY spread DESC, Title;

-- Q9
SELECT avg(a.stars) - avg(b.stars) as Different
FROM
(SELECT Movie.title, avg(Rating.stars) as stars
    FROM Rating join Movie on Rating.mID = Movie.mID
    WHERE Movie.year < 1980
    GROUP BY Movie.title) as a,
(SELECT Movie.title, avg(Rating.stars) as stars
    FROM Rating join Movie on Rating.mID = Movie.mID
    WHERE Movie.year >= 1980
    GROUP BY Movie.title) as b;