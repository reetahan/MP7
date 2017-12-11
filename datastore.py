import pickledb

db = pickledb.load('realmp7data.db', False)

def passData(name, preferences, time, id):
    namepreftime = [name, preferences, time]
    db.set(id,namepreftime)

def returnData(id):
    return db.get(id)
