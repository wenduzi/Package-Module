filename = 'people-record'


def storerecord(db, filename=filename):
    with open(filename, 'w') as f:
        for key in db.keys():
            f.write(key + '\n')
            # need annotate
            for (name, value) in db[key].items():
                f.write(name + ' ==> ' + repr(value)+'\n')
            f.write('endrec.\n')
        f.write('enddb.')


def loadrecord(filename=filename):
    with open(filename, 'r') as f:
        db = {}
        rec = {}
        for char in f.readlines():
            if char != 'enddb':
                name,value = char.split(' ==> ')
                rec[name] = value
            db[char] = rec
            print char




if __name__ == '__main__':
    # from initdata import db
    # storerecord(db)
    loadrecord(filename)
