# import the psycopg2 database adapter for PostgreSQL
from psycopg2 import connect, Error
import json

from psycopg2.extras import Json
from psycopg2.extras import json as psycop_json
import sys
with open('data.json') as json_data:
    record_list = json.load(json_data)
sql_string = 'INSERT INTO {} '.format( 'json_data')

first_record = record_list[0]

columns = list(first_record.keys())
print ("\ncolumn names:", columns)

# if just one dict obj or nested JSON dict
