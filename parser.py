from db import *
from log_parser import *
import bz2
import sqlite3
from pprint import pprint
from optparse import OptionParser

if __name__ == '__main__':

    db_path = 'db/2024.db'
    parser = OptionParser()

    parser.add_option("-p", "--db-path",type="string", help="DB Path")
    parser.add_option("-l", "--limit",type="string", help="Limit")
    parser.add_option("-o", "--offset",type="string", help="Offset")

    opts,_ = parser.parse_args() 

    lp = LogParser()
    


    num_logs = get_total_logs_count(db_path)
    print(num_logs)  # Prints: '216880'

    loaded_logs = load_logs_from_db(db_path, limit=opts.limit, offset=opts.offset)  # Not sure how LIMIT and OFFSET works here? Dates?
    print('Number of loaded logs:', len(loaded_logs))  # Prints '1' => I retrieved 1 log out of 216880 logs.

    for log in loaded_logs:

        parsed_log = lp.split_log_to_game_rounds(log['log_content'])

        print('LOG:')
        pprint(log)

        print('\nPARSED LOG:')
        pprint(parsed_log)