from db import *
from log_parser import *

from optparse import OptionParser

if __name__ == '__main__':

    db_path = 'db/2024.db'
    parser = OptionParser()

    parser.add_option("-p", "--db-path",type="string", help="DB Path")
    parser.add_option("-l", "--limit",type="string", help="Limit")
    parser.add_option("-o", "--offset",type="string", help="Offset")

    opts,_ = parser.parse_args() 

    lp = LogParser()
    


    loaded_logs = load_logs_from_db(db_path, limit=opts.limit, offset=opts.offset)  # Not sure how LIMIT and OFFSET works here? Dates?
    
    for log in loaded_logs:
        filename = log['log_id'] + ".xml"
        f = open(filename, "w")
        f.write(log['log_content'])
        f.close()
    
    