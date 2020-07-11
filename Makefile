deploy:
	git push heroku master

lint:
	pylint *.py */*.py

run:
	streamlit run app.py