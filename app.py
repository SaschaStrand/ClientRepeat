from flask import Flask, render_template
from clients import Clients

app = Flask(__name__)

Clients = Clients()

#Index
@app.route('/')
def index():
  return render_template('main.html')

#New Appointment (newAppt)
@app.route('/newAppt')
def newAppt():
  return render_template('newAppt.html')

#Clients 
@app.route('/clients')
def clients():
  return render_template('clients.html', clients = Clients)

#Reports
@app.route('/reports')
def reports():
  return render_template('reports.html')

if __name__ == '__main__':
  app.run(debug=True)
