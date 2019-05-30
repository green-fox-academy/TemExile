import json
import psycopg2
import insertmessage
import insertmentions
import insertuser
import insertreaction

with open('gfa-team-thanks.json', encoding = 'UTF-8', mode = 'r') as jinfile:
    raw_data = json.load(jinfile)

# remove the record that is a file_comment
raw_data.pop(599)

insertmessage.add_to_message(raw_data)
insertuser.add_to_users(raw_data)
insertreaction.add_to_reactions(raw_data)
insertmentions.add_to_mention(raw_data)