from flask import Blueprint, render_template
from flask_login import login_required
from .models import Document
from . import db

main = Blueprint("main", __name__)

@main.route('/')
@login_required
def index():
    doc = Document.query.first()
    if not doc:
        doc = Document(content="")
        db.session.add(doc)
        db.session.commit()
    return render_template('index.html', content=doc.content)
