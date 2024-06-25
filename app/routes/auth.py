from flask import Blueprint, request, jsonify, flash
from flask_login import login_user, logout_user, current_user, login_required  # Import Flask-Login functions
from app import db, bcrypt  # Import db and bcrypt instances from app package
from app.models.user import User  # Import the User model



bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/login', methods=['POST'])
def login():
    if current_user.is_authenticated:
        return jsonify({'message': 'Already logged in'}), 200
    
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    
    if not username or not password:
        return jsonify({'error': 'Missing username or password'}), 400
    
    user = User.query.filter_by(username=username).first()
    if user is None or not user.check_password(password):
        return jsonify({'error': 'Invalid username or password'}), 401
    
    login_user(user)
    return jsonify({'message': 'Login successful'}), 200

@bp.route('/logout', methods=['POST'])
def logout():
    logout_user()  # Log the user out
    return jsonify({'message': 'Logout successful'}), 200  # Return success message


@bp.route('/register', methods=['POST'])
def register():
    try:
        data = request.get_json()
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')
        
        # Check if username or email already exists
        existing_user = User.query.filter_by(username=username).first()
        existing_email = User.query.filter_by(email=email).first()
        
        if existing_user:
            return jsonify({"error": {"username": "Username already exists"}}), 400
        if existing_email:
            return jsonify({"error": {"email": "Email address already registered"}}), 400
        
        # Create new user
        user = User(username=username, email=email)
        user.set_password(password)
        
        db.session.add(user)
        db.session.commit()
        
        return jsonify({"message": "Registration successful"}), 200
    
    except Exception as e:
        return jsonify({"error": str(e)}), 400