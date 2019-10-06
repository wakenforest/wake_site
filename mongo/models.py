from django.db import models

# Create your models here.
import mongoengine
# from typeidea.settings.develop import DBNAME 
# DBNAME='mongotest'
# mongoengine.connect(DBNAME)  

class MongoModel(mongoengine.Document):
    _id = mongoengine.IntField(default=0)
    id = mongoengine.IntField(default=0)
    value = mongoengine.IntField(default=0)
    Date = mongoengine.DateTimeField(auto_now_add=True, verbose_name="时间")

    meta = {
        # 'collection': 'area'
        'collection': 'data',
        'strict': False,
    }