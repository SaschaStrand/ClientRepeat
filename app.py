from flask import Flask, render_template, g, request, flash, redirect, url_for
import MySQLdb
from werkzeug.security import generate_password_hash, check_password_hash

# Configure database
app = Flask(__name__)
db = MySQLdb.connect("localhost", "root", "YayClientRepeat!", "ClientRepeat")
loggedIn = False
activeUser = ""

#Index
@app.route('/')
def index():
  return render_template('main.html')

#Register
@app.route('/register')
def register():
  return render_template('register.html')

#Register Process
@app.route('/registerProcess', methods=['POST'])
def registerProcess():
    global loggedIn
    global activeUser
    if loggedIn:
        cur = db.cursor()
        msg = 'there was a serious error'
        try:
            username = request.form['username']
            cur.execute("SELECT * FROM USERS WHERE username = %s", [username])
            foo = cur.fetchone()
            print foo
            if foo:
                print "huh"
                raise Exception
        except:
            msg = 'That username is already in use. Please choose another.'
            return render_template("registerResult.html", msg=msg)
            cur.close()

        try:
            password = request.form['password']
            password = generate_password_hash(password)
            cur.execute("INSERT INTO USERS (username, password) VALUES (%s,%s);", (username, password))
            db.commit()
            msg = "You are now a user!"
            return render_template("loginFailResult.html", msg=msg)
            cur.close()
        except:
            db.rollback()
            msg = "Something has gone wrong inserting your new user credentials into the database."
            return render_template("registerResult.html", msg=msg)
            cur.close()
    else:
        msg = "This page is available only to registerd users."
        return render_template('loginFailResult.html', msg=msg)

#Login
@app.route('/login')
def login():
  return render_template('login.html')

#Login Process
@app.route('/loginProcess', methods=['POST'])
def loginProcess():
    global loggedIn
    global activeUser
    #if form.validate():
    cur = db.cursor()
    msg = 'Something has gone wrong processing your credentials.'
    try:
        username = request.form['username']
        cur.execute("SELECT * FROM USERS WHERE username = %s", [username])
        data = cur.fetchone()
        if not data:
            raise Exception
    except:
        msg = 'Invalid credentials'
        return render_template("loginFailResult.html", msg=msg)
        cur.close()

    candidate_password = request.form['password']
    password = data[1]
    if check_password_hash(password, str(candidate_password)):
        loggedIn = True
        activeUser = username
        msg = "You were successfully logged in"
        cur.close()
        return render_template('newAppt.html')
    else:
        msg = 'Invalid credentials'
        return render_template("loginFailResult.html", msg=msg)
        cur.close()

#New Appointment (newAppt)
@app.route('/newAppt')
def newAppt():
    global loggedIn
    global activeUser
    if loggedIn:
        return render_template('newAppt.html')
    else:
        msg = "This page is available only to registerd users."
        return render_template('loginFailResult.html', msg=msg)

#New Appt Process
@app.route('/newApptProcess', methods=['POST'])
def newApptProcess():
    global loggedIn
    global activeUser
    if loggedIn:
      cur = db.cursor()
      msg = 'there was a serious error'
      try:
          try:
              full_name = request.form['full_name']
              cur.execute("SELECT * FROM CLIENTS WHERE full_name = %s", [full_name])
              foo = cur.fetchall()
              if not foo[0]:
                  raise Exception
          except:
              msg = 'Please make sure the client you entered is in your client list'
          appt_date = request.form['date']
          duration = request.form['duration']
          reschedule = request.form['reschedule']
          tip = request.form['tip']
          cur.execute("INSERT INTO appts (full_name, appt_date, duration, reschedule, tip) VALUES (%s,%s,%s,%s,%s);", (full_name, appt_date, duration, reschedule, tip))
          print "about to commit"
          db.commit()
          msg = "Record successfully added"
      except:
          db.rollback()
          msg = "error in insert operation"
      finally:
          return render_template("newApptResult.html", msg=msg)
          cur.close()

#Clients
@app.route('/clients')
def clients():
    global loggedIn
    global activeUser
    if loggedIn:
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
    else:
        msg = "This page is available only to registerd users."
        return render_template('loginFailResult.html', msg=msg)

#Add Clients
@app.route('/addClient', methods=['GET', 'POST'])
def addClients():
    global loggedIn
    global activeUser
    if loggedIn:
        return render_template('addClients.html')
    else:
        msg = "This page is available only to registerd users."
        return render_template('loginFailResult.html', msg=msg)

#Add Client Process
@app.route('/addClientProcess', methods=['POST'])
def addClientProcess():
    global loggedIn
    global activeUser
    if loggedIn:
        cur = db.cursor()
        msg = 'there was a serious error'
        try:
            full_name = request.form['first_name'] + " " + request.form['last_name']
            phone = request.form['phone']
            email = request.form['email']
            cur.execute("INSERT INTO clients (full_name, phone, email) VALUES (%s,%s,%s);", (full_name, phone, email))
            db.commit()
            msg = "Record successfully added"
        except:
            db.rollback()
            msg = "error in insert operation"
        finally:
            return render_template("addClientResult.html", msg=msg)
            cur.close()

#Reports
@app.route('/reports')
def reports():
    global loggedIn
    global activeUser
    if loggedIn:
        return render_template('reports.html')
    else:
        msg = "This page is available only to registerd users."
        return render_template('loginFailResult.html', msg=msg)

#Scheduling Reports
@app.route('/schedulingReports')
def schedulingReports():
    global loggedIn
    global activeUser
    if loggedIn:
        return render_template('schedulingReports.html')
    else:
        msg = "This page is available only to registerd users."
        return render_template('loginFailResult.html', msg=msg)

#Logout
@app.route('/logout')
def logout():
    global loggedIn
    global activeUser
    loggedIn = False
    activeUser = ""
    return render_template('main.html')

if __name__ == '__main__':
  app.run(
  debug=True
  )
