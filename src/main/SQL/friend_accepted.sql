-- Table request_accepted holds the data of friend acceptance, while requester_id and accepter_id both are the id of a person.
-- | requester_id | accepter_id | accept_date|
-- |--------------|-------------|------------|
-- | 1            | 2           | 2016_06-03 |
-- | 1            | 3           | 2016-06-08 |
-- | 2            | 3           | 2016-06-08 |
-- | 3            | 4           | 2016-06-09 |
-- Write a query to find the the people who has most friends and the most friends number.

-- solution 1:
SELECT a.id
	,sum(a.counts) AS num
FROM (
	SELECT requester_id AS id
		,count() AS counts
	FROM request_accepted
	GROUP BY requester_id

	UNION ALL

	SELECT accepter_id AS id
		,count() AS counts
	FROM request_accepted
	GROUP BY accepter_id
	) a
GROUP BY a.id
ORDER BY num DESC limit 1

-- solution 2:
SELECT tup.user1
	,count(DISTINCT tup.user2) AS num_friends
FROM (
	SELECT DISTINCT requester_id AS user1
		,accepter_id AS user2
	FROM request_accepted

	UNION

	SELECT DISTINCT accepter_id AS user1
		,requester_id AS user2
	FROM request_accepted
	) tup
GROUP BY tup.user1
ORDER BY count(tup.user2) DESC
