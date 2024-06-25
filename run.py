# run.py

from app import create_app  # Import create_app function from app package

app = create_app()  # Create an instance of the Flask application

if __name__ == '__main__':
    app.run(debug=True)  # Run the application if executed directly
