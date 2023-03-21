import sys, getopt
import couchdb
import json

def main(argv):
    inputfile = ''
    dbname = ''
    opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
    for opt, arg in opts:
        if opt == '-h':
            print ('main.py -i <inputfile> -o <dbname>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            dbname = arg
    print ('Input file is ', inputfile)
    print ('Database Name is ', dbname)
    
    couch = couchdb.Server('http://admin:admin@localhost:5984/')
    db = couch.create(dbname) # newly created

    data = []
    i = 0
    with open(inputfile) as f:
        for line in f:

            if line[-2] == ",":
                line = line[0:-2]

            jsonData = json.loads(line)
            doc = jsonData['doc']
            doc.pop('_rev')
            doc.pop('_id')

            db.save(doc)

            i += 1
            print ('Processing =>', i)
    
if __name__ == "__main__":
   main(sys.argv[1:])
