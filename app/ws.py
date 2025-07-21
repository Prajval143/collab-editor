from flask_socketio import emit
from .models import Document, db
from .ai import ai_suggestion

def socketio_events(socketio):
    @socketio.on("edit")
    def handle_edit(data):
        content = data["content"]
        doc = Document.query.first()
        doc.content = content
        db.session.commit()
        suggestion = ai_suggestion(content)
        emit("update", {"content": content, "suggestion": suggestion}, broadcast=True)
