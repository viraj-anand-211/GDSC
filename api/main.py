from flask import Flask, request, jsonify, render_template
import asyncio
import aiosqlite

from database_helper import *

app = Flask(__name__)

init_db()
 
@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/data_update', methods=['POST'])
def data_update():
    if request.method == 'GET':
        return "invalid request type", 500
    try:
        json_data = request.get_json()
        location = json_data.get('location')
        value = json_data.get('value')
        ret = insert_or_update_location(location, value)
        if ret:
            return jsonify({"data":"created new entry", "id": ret})
        return jsonify({"data":"entry updated"})
        
    except:
        return "invalid data format"
    
    
@app.route('/get-data', methods = ['POST'])
def get_data():
    data = get_from_database()
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)