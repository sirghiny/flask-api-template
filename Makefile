env:
	rm -Rf venv && virtualenv venv && source venv/bin/activate && pip install --upgrade pip && pip install --upgrade -r requirements.txt

run:
	source venv/bin/activate && source .env && python run.py

test:
	source venv/bin/activate && source .env && python -m pytest

db:
	rm -Rf migrations && source venv/bin/activate && source .env && python manage.py db init && python manage.py db migrate && python manage.py db upgrade