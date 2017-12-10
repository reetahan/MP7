from tinydb import TinyDB, Query

db = TinyDB('mp7data.json')


def passData(name, preferences, time):
    preftime = [preferences, time]
    id = db.insert({name:preftime})
    return id

def returnData(id):
    for item in db:
        if(item.doc_id == id):
            return item
