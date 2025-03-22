from app import app, db  # Replace with your actual module name

# Create all tables
with app.app_context():
    db.create_all()
