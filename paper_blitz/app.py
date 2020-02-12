from paper_blitz.config import app, db
from paper_blitz.survey.routes import add_vote, get_articles_survey

@app.route('/')
def hello_world():
	return 'Hello World!'

if __name__ == '__main__':
    app.run(debug=False)