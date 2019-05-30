-- /message information regarding the message
SELECT a.id as Message_ID, a.user_id as Poster, a.message as Content, count(b.id) as Reactions
FROM messages a join reactions b on a.id = b.message_id
GROUP BY a.id, b.message_id
ORDER BY count(b.id) DESC;

-- /user/message information regarding each user on message and reaction
SELECT a.user_id, count(b.id) as messages
FROM users a left join messages b on a.user_id = b.user_id
GROUP BY a.user_id
ORDER BY count(b.id) DESC;

-- /user/reaction
SELECT a.user_id, count(b.id) as reactions
FROM users a left join reactions b on a.user_id = b.user_id
GROUP BY a.user_id
ORDER BY count(b.id) DESC;

-- /reaction information regarding the emoji
SELECT reaction, count(reaction) as Used
FROM reactions
GROUP BY reaction
ORDER BY count(reaction) DESC;

-- /message/reaction
SELECT a.id as Message_ID, count(b.id) as reacctions
FROM messages a left join reactions b on a.id = b.message_id
GROUP BY a.id, b.message_id
ORDER BY count(b.id) DESC;