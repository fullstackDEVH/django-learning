import datetime
from .schemas.activities import Activities

def my_scheduled_job():
  Activities.objects.create(data = {"huy" : "abc", "user_id" : "7e26eec1-cedf-44f8-8dbd-3bc3c4f1fd8f"})
  