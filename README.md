python3 -m vevn venv
source venv/bin/activate
pip install -r requirements.txt
cd mysite/
docker run -p 6379:6379 -d redis:5
python manage.py runserver