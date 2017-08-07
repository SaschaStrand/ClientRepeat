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

#Income Reports
@app.route('/incomeReports')
def incomeReports():
  return render_template('incomeReports.html')

#Scheduling Reports
@app.route('/schedulingReports')
def schedulingReports():
  return render_template('schedulingReports.html')

if __name__ == '__main__':
  app.run(debug=True)
