# Collab-Editor

Collab-Editor is a web-based collaborative text editor built with Flask. It enables multiple users to edit documents in real time, supports user authentication, and integrates AI-powered features.

## Features

- Real-time collaborative editing via WebSockets
- User registration and login
- Document management
- AI-powered text suggestions and summarization
- Secure session management

## Project Structure

```
collab-editor/
│
├── run.py                  # Entry point for the Flask app
├── config.py               # App configuration
├── requirements.txt        # Python dependencies
├── .gitignore              # Git ignore rules
├── README.md               # Project documentation
├── Technical_Documentation_and Design_Decision.txt
│
├── app/
│   ├── __init__.py         # App initialization and blueprint registration
│   ├── models.py           # Database models
│   ├── auth.py             # Authentication logic
│   ├── routes.py           # HTTP routes
│   ├── ws.py               # WebSocket collaboration logic
│   ├── ai.py               # AI feature integration
│   ├── static/
│   │   └── style.css       # CSS styles
│   └── templates/
│       ├── index.html      # Main editor UI
│       ├── login.html      # Login page
│       └── register.html   # Registration page
│
└── instance/
    └── db.sqlite3          # SQLite database
```

## Getting Started

1. **Install dependencies:**
   ```
   pip install -r requirements.txt
   ```

2. **Run the application:**
   ```
   python run.py
   ```

3. **Access the editor locally:**
   Open your browser and go to `http://localhost:5000`

## Live Demo

You can try Collab-Editor online:

- **Register:** [https://collab-editor-rhfi.onrender.com/register](https://collab-editor-rhfi.onrender.com/register)
- **Login:** [https://collab-editor-rhfi.onrender.com/login](https://collab-editor-rhfi.onrender.com/login)
- **Use the Editor:** [https://collab-editor-rhfi.onrender.com/](https://collab-editor-rhfi.onrender.com/)

## Design Decisions

- Modular codebase for maintainability and scalability
- Flask blueprints for route and feature isolation
- WebSocket support for real-time collaboration
- SQLite for simple development setup
- Separation of static assets and templates

## Challenges Faced

- Real-time document synchronization and conflict resolution
- Secure session management with concurrent WebSocket connections
- Scalability limitations of SQLite and WebSocket architecture
- Asynchronous AI integration
- Protection against common web vulnerabilities

## License

This project is for educational