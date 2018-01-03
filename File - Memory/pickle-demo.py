import pickle
import glob


def storerecord(db):
    for key, record in db.items():
        with open(key+'.pk1', 'wb') as f:
            pickle.dump(record, f)


def updaterecord():
    for filename in glob.glob('*.pk1'):
        with open(filename, 'rb') as f:
            record = pickle.load(f)
            if filename == 'pickle-wen.pk1':
                with open(filename, 'wb') as w:
                    record['pay'] *= 3
                    pickle.dump(record, w)
            print filename, record


if __name__ == '__main__':
    from initdata import db
    storerecord(db)
    #updaterecord()
