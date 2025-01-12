# Starting of the app 


from flask import Flask 
from backend.models import db

app = None
def setup_app():
    app=Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///ticket_show.sqlite3"
    db.init_app(app)     
    #Pending here is sqlite connection]
    app.app_context().push()# direct access to other modules
    app.debug=True
    print("Ticket show app is Starting...")

setup_app()

from backend.controllers import * 

if __name__=='__main__':
    app.run()

