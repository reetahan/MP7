import datetime
from subredditsCall import datastore
from subredditsCall import reddit


def timer(time, id):
    hour = time/3600
    found_time = False

    while(not(found_time)):
        now = datetime.datetime.now()
        todays_hour = now.replace(hour=time, minute=0, second=0, microsecond=0)
        if(now == todays_hour):
            f = datastore.returnData(id)[1]
            return reddit.pick_sub(f)




