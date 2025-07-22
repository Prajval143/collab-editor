from flask_socketio import emit
from .models import Document, db
from .ai import ai_suggestion
import requests



def get_suggestion(text):
    try:
        res = requests.post(
            "https://api.languagetool.org/v2/check",
            data={
                'text': text,
                'language': 'en-US'
            }
        )
        matches = res.json().get("matches", [])
        if matches:
            return matches[0]["message"]
        return ""
    except Exception as e:
        print("Suggestion error:", e)
        return ""
    

def socketio_events(socketio):
    @socketio.on("edit")
    def handle_edit(data):
        content = data["content"]
        doc = Document.query.first()
        doc.content = content
        db.session.commit()
        snippet = content[-200:] if len(content) > 200 else content
        suggestion = get_suggestion(snippet)
        emit("update", {"content": content, "suggestion": suggestion}, broadcast=True, include_self=False)
