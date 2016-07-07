migrate:
	- python hoomi/manage.py makemigrations users jobs
	- python hoomi/manage.py migrate
