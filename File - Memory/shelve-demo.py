import shelve

filename='shelve-demo.pk1'


def initdata():
    db = shelve.open(filename)
    wen = {'name': 'wenduzi' , 'age': 18 , 'pay': 50000 , 'job': 'dev'}
    li = {'name': 'lilei' , 'age': 16 , 'pay': 30000 , 'job': 'hdw'}
    han = {'name': 'hanmeimei' , 'age': 15 , 'pay': 20000 , 'job': None}
    db['wen'] = wen
    db['li'] = li
    db['han'] = han
    db.close()


def updata():
    db = shelve.open(filename)
    wen = db['wen']
    wen['pay'] *= 3
    db['wen']= wen
    print db
    db.close()



if __name__ == '__main__':
    #initdata()
    updata()