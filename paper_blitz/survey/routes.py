#!flask/bin/python3
from paper_blitz.articles.article import Article
from paper_blitz.stack.model import Stack, Participant, Group
from paper_blitz.stack.schema import Article_Stack_Schema
from paper_blitz.survey.model import Vote
from paper_blitz.survey.create_survey import Article_Selector_Survey
from flask import jsonify, abort, request

from paper_blitz.config import app, db


@app.route('/api/v0.1/vote/submit', methods=['POST'])
def add_vote():
    """
    Creates a new article
    """
    article_name = request.json.get('article_name','')
    username = request.json.get('username','')
    user = Participant.query.find(Participant.username == username).first_or_404()

    article = Article.query.filter(Article.name == article_name).first_or_404()
    group = user.group   
    stack_entry = Stack.query.filter(Stack.article == exist_article & Stack.group == group).first_or_404()
    
    vote = Vote(voter = user, article = stack_entry)
    db.session.add(vote)
    db.session.commit()

    return f"Vote added for {user} on {article}", 201

@app.route('/api/v0.1/survey/get', methods=['GET'])
def get_articles_survey():
    """
    Get articles of survey
    """
    if 'groupname' in request.args:
        groupname = request.args['groupname']
    else:
        return "Error: no groupname provided, please provide one."
    print("OK")
    group = Group.query.filter(Group.name == groupname).first_or_404()

    article_selector = Article_Selector_Survey()
    new_stack_entries, old_stack_entries = article_selector.select_articles(group)
    
    schema = Article_Stack_Schema(many = True)
    dump = {"old" : schema.dump(new_stack_entries), "new" : schema.dump(old_stack_entries)}
    return jsonify(dump), 201
    


