from db import *
from log_parser import *

from optparse import OptionParser

if __name__ == '__main__':

    parser = OptionParser()

    parser.add_option("-p", "--path",type="string", help="DB Path")
    parser.add_option("-l", "--limit",type="string", help="Limit")
    parser.add_option("-o", "--offset",type="string", help="Offset")
    parser.add_option("-f", "--format", type="string", help="If On, split files into hanchans", default="")
    parser.add_option("-n", "--fname", type="string", help="Name of the Output File")

    opts,_ = parser.parse_args() 

    lp = LogParser()
    


    loaded_logs = load_logs_from_db(opts.path, limit=opts.limit, offset=opts.offset)  # Not sure how LIMIT and OFFSET works here? Dates?
    
    print("This DB has %d games in total" % get_total_logs_count(opts.path))
    
    print(loaded_logs)
    
   # if(opts.format):
   #     for log in loaded_logs:
   #        filename = log['log_id'] + ".xml"
   #        f = open(filename, "w")
   #        f.write(log['log_content'])
   #        f.close()
   # 
   # 
   # else:
   #     filename =  opts.fname + ".xml" if opts.fname else opts.path.removesuffix(".db") + ".xml"
   #     f = open(filename, "w")
   #     for log in loaded_logs:
   #         f.write(log['log_id'] + "\n" + log['log_content'] + "\n")
   #     f.close()
    