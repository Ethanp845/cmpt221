"""app.py: render and route to webpages"""

import os
from flask import Flask, render_template

def create_app():
    """Create Flask application"""
    # create flask app
    app = Flask(__name__, 
                template_folder=os.path.join(os.getcwd(), 'templates'), 
                static_folder=os.path.join(os.getcwd(), 'static'))
    
    # ===============================================================
    # routes
    # ===============================================================

    @app.route('/')
    def index():
        """6 or 7"""
        return render_template('index.html')
    
    @app.route('/page2')
    def page2():
        """BRAINROT WEBSITE"""
        return render_template('page2.html')
    
    @app.route('/page3')
    def page3():
        """67676767676767"""
        return render_template('page3.html')

    return app

if __name__ == "__main__":
    app = create_app()
    # debug refreshes your application with your new changes every time you save
    app.run(debug=True)