# -*- coding: utf-8 -*-
"""
Created on Thu May 16 18:43:29 2024

@author: chandana sasumana
"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import date
from datetime import datetime, date
from models import db, BotLogs  # Import the Subscription class
from tabulate import tabulate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Chandana%402004@localhost/data1'
db.init_app(app)

from models import BotLogs  # Import your model

@app.route('/populate-db')
def populate_db():
    # Create dummy subscription records
    dummy_botlogs = [
        BotLogs(
            mobile_number='8797676771',
            log='Silver',
            timestamp=datetime.utcnow(),  # Assuming the primary user ID
        ),
        BotLogs(
            mobile_number='8797676971',
            log='Sillver',
            timestamp=datetime.utcnow(),  # Assuming the primary user ID
            
        )
    ]

@app.route('/botlogs')
def show_botlogs():
    # Query the BotLogs table to get all records
    botlogs = BotLogs.query.all()
    
    # Prepare the table headers
    headers = ["ID", "Mobile Number", "Log", "Timestamp"]
    
    # Prepare a list of lists representing the table data
    table_data = [[botlog.id, botlog.mobile_number, botlog.log, botlog.timestamp] for botlog in botlogs]

    # Generate the table using the tabulate module
    table = tabulate(table_data, headers=headers, tablefmt="grid")

    # Return the table data as HTML
    return table

if __name__ == '__main__':
    app.run(debug=True)
    

    


