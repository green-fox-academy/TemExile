-- Q1
SELECT b.starttime FROM cd.bookings b join cd.members a on a.memid = b.memid
WHERE a.surname = 'Farrell' and a.firstname = 'David';

-- Q2
SELECT a.starttime, b.name
FROM cd.bookings a inner join cd.facilities b on a.facid = b.facid
WHERE a.starttime >= '2012-9-21' and a.starttime < '2012-09-22' and b.name LIKE 'Tennis%'
ORDER BY a.starttime;

-- Q3
SELECT distinct a.firstname, a.surname
FROM cd.members a inner join cd.members b on a.memid = b.recommendedby
ORDER BY a.surname, a.firstname;

-- Q4
SELECT a.firstname as mfirstname, a.surname as msurname, b.firstname as rfirstname, b.surname as rsurname
FROM cd.members a left join cd.members b on a.recommendedby = b.memid
ORDER BY msurname, mfirstname

-- Q5
SELECT distinct concat(a.firstname, ' ', a.surname)  as member, c.name as facility
FROM cd.members a inner join cd.bookings b on a.memid = b.memid 
				inner join cd.facilities c on b.facid = c.facid
WHERE c.name LIKE 'Tennis%'
ORDER BY member;

-- Q6
SELECT concat(a.firstname, ' ', a.surname) as member, c.name as facility,
	case when a.memid = 0 then
				b.slots * c.guestcost
		else
				b.slots * c.membercost
		end as cost
FROM cd.members a inner join cd.bookings b on a.memid = b.memid
					inner join cd.facilities c on b.facid = c.facid
WHERE (b.starttime >= '2012-09-14' and b.starttime < '2012-09-15')
		and (
		(a.memid = 0 and b.slots * c.guestcost > 30) or
		(a.memid != 0 and b.slots * c.membercost > 30))
ORDER BY cost DESC;

-- Q7
SELECT distinct concat(a.firstname, ' ', a.surname) as member,
		(SELECT concat(b.firstname, ' ', b.surname)
		 FROM cd.members b
		 WHERE a.recommendedby = b.memid)
FROM cd.members a;

-- Q8
SELECT member, facility, cost 
FROM
	(SELECT concat(a.firstname, ' ', a.surname) as member, c.name as facility,
		case when a.memid = 0 then
					b.slots * c.guestcost
			else
					b.slots * c.membercost
			end as cost
	FROM cd.members a inner join cd.bookings b on a.memid = b.memid
					inner join cd.facilities c on b.facid = c.facid
	WHERE b.starttime >= '2012-09-14' and b.starttime < '2012-09-15')  as table1
WHERE cost > 30
ORDER BY cost DESC;

