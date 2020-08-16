from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
"""
class Booking(models.Model):
	id = models.Column(db.Integer, primary_key=True)
	bname = models.Column(db.String(50), nullable=False)
	baddress = models.Column(db.Text, nullable=False)
	bcontact = models.Column(db.String, nullable=False)
	bresort = models.Column(db.String, nullable=False)
	bref = models.Column(db.String, nullable=False, default='Self')
	bdate = models.Column(db.DateTime, nullable=False, default=datetime.utcnow)
	bdaynight = models.Column(db.String, nullable=False)
	brentcat = models.Column(db.String, nullable=False)
	bcat = models.Column(db.String, nullable=False, default='Self')
	bcatveg = models.Column(db.String, nullable=False, default='Veg')
	bgathconf = models.Column(db.Integer,nullable=False)
	bnote = models.Column(db.Text, nullable=False)
	bauth = models.Column(db.String(10), nullable=False, default='No')
	user_id = models.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

	def __repr__(self):
		return f"Booking('{self.bname}'),'{self.baddress}','{self.bcontact}','{self.bref}', '{self.bdate}', '{self.bdaynight}', '{self.brentcat}','{self.bcat}','{self.bcatveg}','{self.bgathconf}', '{self.bnote}')"

"""


# Create your models here.
