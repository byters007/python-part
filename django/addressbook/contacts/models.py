from django.db import models
from django.core.urlresolvers import reverse
import csv

data = []
with open('./contacts/data_u-2012.csv' , 'r') as csvfile :
	reader = csv.reader(csvfile ,delimiter=';')
	for row in reader:
		data.append(row)

for x in range(len(data)):
	data[x][0] = data[x][2] +"-"+ data[x][0]+"-" + data[x][1]



YEAR_IN_SCHOOL_CHOICES = (
	('FR', 'Freshman'),
	('SO', 'Sophomore'),
	('JR', 'Junior'),
	('SR', 'Senior'),
)


class Contact(models.Model):
	progs = [''] * len(data)

	PROGRAMME_CHOICES =()
	for x in range(len(progs)):
		PROGRAMME_CHOICES = ((progs[x], data[x][0]),) + PROGRAMME_CHOICES
	PROGRAMME_CHOICES = PROGRAMME_CHOICES[::-1]

	first_name = models.CharField(
		max_length=255,
	)

	last_name = models.CharField(
		max_length=255,

	)

	programme = models.CharField( 
		max_length=6,choices=PROGRAMME_CHOICES,
		default='B4110')


	email = models.EmailField()

	def __str__(self):

		return ' '.join([
			self.first_name,
			self.last_name,
		]) 

	def get_absolute_url(self):

		return reverse('contacts-view', kwargs={'pk': self.id})

class Address(models.Model):

	contact = models.ForeignKey(Contact)
	address_type = models.CharField(
		max_length=10,
	)

	address = models.CharField(
		max_length=255,
	)
	city = models.CharField(
		max_length=255,
	)
	state = models.CharField(
		max_length=2,
	)
	postal_code = models.CharField(
		max_length=20,
	)

	class Meta:
		unique_together = ('contact', 'address_type',)


