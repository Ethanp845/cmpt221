"""app.py: render and route to webpages"""

import os
import logging
from dotenv import load_dotenv
from flask import Flask, render_template, request, redirect, url_for
from db.query import get_all
from db.server import init_database
from db.schema import Users

# load environment variables from .env
load_dotenv()

# setup logging
logging.basicConfig(
    filename="logs/log.txt",
    level=logging.INFO,
    filemode="a",
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

# database connection - values set in .env
db_name = os.getenv('db_name')
db_owner = os.getenv('db_owner')
db_pass = os.getenv('db_pass')
db_url = f"postgresql://{db_owner}:{db_pass}@localhost/{db_name}"

def create_app():
    """Create Flask application and connect to your DB"""
    # create flask app
    app = Flask(__name__, 
                template_folder=os.path.join(os.getcwd(), 'templates'), 
                static_folder=os.path.join(os.getcwd(), 'static'))
    
    # connect to db
    app.config["SQLALCHEMY_DATABASE_URI"] = db_url
    
    # Initialize database
    with app.app_context():
        if not init_database():
            print("Failed to initialize database. Exiting.")
            exit(1)

    # ===============================================================
    # routes
    # ===============================================================

    @app.route('/')
    def index():
        """Home page"""
        return render_template('index.html')
    
    @app.route('/signup', methods=['GET', 'POST'])
    def signup():
        """Sign up page: enables users to sign up"""
        if request.method == 'POST':
            # server-side validation
            is_valid = True
            error_msg = ""
            
            # get form data
            first_name = request.form.get('FirstName', '').strip()
            last_name = request.form.get('LastName', '').strip()
            email = request.form.get('Email', '').strip()
            phone = request.form.get('PhoneNumber', '').strip()
            password = request.form.get('Password', '').strip()
            
            # validation checks
            if not first_name or not last_name or not email or not phone or not password:
                is_valid = False
                error_msg = "All fields are required"
            
            # check first name only contains letters
            elif not first_name.isalpha():
                is_valid = False
                error_msg = "First name can only contain letters"
            
            # check last name only contains letters  
            elif not last_name.isalpha():
                is_valid = False
                error_msg = "Last name can only contain letters"
            
            # check phone number is 10 digits
            elif not phone.isdigit() or len(phone) != 10:
                is_valid = False
                error_msg = "Phone number must be 10 digits"
            
            # if valid, try to insert into database
            if is_valid:
                try:
                    # TODO: Add actual database insertion here
                    # For now, just log the attempt
                    logger.info(f"Signup attempt for email: {email}")
                    
                    # In a real implementation, you would hash the password here
                    # hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
                    
                    return redirect(url_for('success'))
                    
                except Exception as e:
                    logger.error(f"Database error during signup: {e}")
                    return render_template('error.html', 
                                         error="Something went wrong. Please try again later.")
            else:
                logger.warning(f"Invalid signup attempt: {error_msg}")
                return render_template('signup.html', error=error_msg)
        
        return render_template('signup.html')
    
    @app.route('/login', methods=['GET', 'POST'])
    def login():
        """Log in page: enables users to log in"""
        
        if request.method == 'POST':
            # get and sanitize form data
            email = request.form.get('email', '').strip()
            password = request.form.get('password', '').strip()
            
            # validation checks
            if not email or not password:
                return render_template('login.html', error="Email and password are required")
            
            # try to find user in database
            try:
                all_users = get_all(Users)
                user_found = None
                
                # search for user by email
                for user in all_users:
                    if user.Email == email:
                        user_found = user
                        break
                
                # check if user exists and password matches
                if user_found and user_found.Password == password:
                    logger.info(f"Successful login for: {email}")
                    return redirect(url_for('success'))
                else:
                    logger.warning(f"Failed login attempt for: {email}")
                    return render_template('login.html', error="Invalid email or password")
                    
            except Exception as e:
                logger.error(f"Login error: {e}")
                return render_template('error.html', 
                                     error="Something went wrong. Please try again later.")
        
        return render_template('login.html')

    @app.route('/users')
    def users():
        """Users page: displays all users in the Users table"""
        try:
            all_users = get_all(Users)
            return render_template('users.html', users=all_users)
        except Exception as e:
            logger.error(f"Error loading users page: {e}")
            return render_template('error.html', 
                                 error="Could not load users. Please try again later.")

    @app.route('/success')
    def success():
        """Success page: displayed upon successful login"""
        return render_template('success.html')
    
    @app.route('/error')
    def error():
        """Error page for generic errors"""
        return render_template('error.html')

    return app

if __name__ == "__main__":
    # Create logs directory if it doesn't exist
    if not os.path.exists('logs'):
        os.makedirs('logs')
    
    app = create_app()
    app.run(debug=True)