-- /message information regarding the message
SELECT a.id as Message_ID, a.user_id as Poster, a.message as Content, count(b.id) as Reactions
FROM messages a join reactions b on a.id = b.message_id
GROUP BY a.id, b.message_id
ORDER BY a.id;