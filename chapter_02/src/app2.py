from flask import Flask
app = Flask(__name__)
from datetime import datetime, date, time, timedelta
from flask import jsonify

@app.route('/')
def hello_world_json_list():
	time=datetime.now()
	data =["Año",time.year,"Mes:",time.month, "Dia",time.day,"hora:",time.hour,"minutos:",time.minute,"segundos: ",time.second,]
	
	return jsonify(data)

if __name__ == '__main__':
    app.run()