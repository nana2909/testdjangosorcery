from django.db import models
from django_sorcery.db import databases


db = databases.get('default')



class Authority(db.Model):
    pk = db.Column(db.Integer(), autoincrement=True, primary_key=True)
    name = db.Column(db.String(lengt=200))

class Form(db.Model):
    pk = db.Column(db.Integer(), autoincrement=True, primary_key=True)
    title = db.Column(db.String(lengt=200))
    context = db.Column(db.String())
    created_at = db.Column(db.DateTime())
    authority = db.ManyToOne(Authority, backref = db.backref("forms", cascade ="all,delete-orphan"))


