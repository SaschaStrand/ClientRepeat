from flask import Flask, render_template, g, request
import MySQLdb

# Configure database
app = Flask(__name__)
db = MySQLdb.connect("localhost", "root", "YayClientRepeat!", "ClientRepeat")

#Index
@app.route('/')
def index():
  return render_template('main.html')

#New Appointment (newAppt)
@app.route('/newAppt')
def newAppt():
  return render_template('newAppt.html')

#New Appt Process
@app.route('/newApptProcess', methods=['POST'])
def newApptProcess():
  #if form.validate():
  cur = db.cursor()
  msg = 'there was a serious error'
  try:
      full_name = request.form['full_name']
      cur.execute("SELECT * FROM CLIENTS WHERE full_name = %s", [full_name])
      foo = cur.fetchall()
      if not foo[0]:
          raise Exception
  except:
      msg = 'Please make sure the client you entered is in your client list'

  try:
      appt_date = request.form['date']
      duration = request.form['duration']
      reschedule = request.form['reschedule']
      tip = request.form['tip']
      print "full_name: %s" % full_name
      print "appt_date: %s" % appt_date
      print "duration: %s" % duration
      print "reschedule: %s" % reschedule
      print "tip: %s" % tip
      cur.execute("INSERT INTO appts (full_name, appt_date, duration, reschedule, tip) VALUES (%s,%s,%s,%s,%s);", (full_name, appt_date, duration, reschedule, tip))
      print "about to commit"
      db.commit()
      msg = "Record successfully added"
  except:
      cur.rollback()
      msg = "error in insert operation"
  finally:
      return render_template("newApptResult.html", msg=msg)
      cur.close()

#Clients
@app.route('/clients')
def clients():
    cur = db.cursor()
    cur.execute("SELECT count(*) FROM clients")
    returnQuant = cur.fetchone()
    if returnQuant[0] > 0:
        cur.execute("SELECT * FROM clients")
        clients = cur.fetchall()
        return render_template('clients.html', clients = clients)
    else:
        return render_template('addClients.html')
        cur.close()

#Add Clients
@app.route('/addClient', methods=['GET', 'POST'])
def addClients():
    return render_template('addClients.html')

#Add Client Process
@app.route('/addClientProcess', methods=['POST'])
def addClientProcess():
    #if form.validate():
    cur = db.cursor()
    msg = 'there was a serious error'
    try:
        full_name = request.form['first_name'] + " " + request.form['last_name']
        phone = request.form['phone']
        email = request.form['email']
        cur.execute("")
        cur.execute("INSERT INTO clients (full_name, phone, email) VALUES (%s,%s,%s);", (full_name, phone, email))
        db.commit()
        msg = "Record successfully added"
    except:
        cur.rollback()
        msg = "error in insert operation"
    finally:
        return render_template("addClientResult.html", msg=msg)
        cur.close()

#Reports
@app.route('/reports')
def reports():
  return render_template('reports.html')

#Scheduling Reports
@app.route('/schedulingReports')
def schedulingReports():
  return render_template('schedulingReports.html')

if __name__ == '__main__':
  app.run(debug=True)
