migrate:
	- python hoomi/manage.py makemigrations users jobs
	- python hoomi/manage.py migrate

test:
	- python hoomi/manage.py test jobs -v2
