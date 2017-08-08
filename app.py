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

#Clients
@app.route('/clients')
def clients():
    cur = db.cursor()
    cur.execute("SELECT count(*) FROM clients")
    returnQuant = cur.fetchone()
    print("Row Quant: {}".format(returnQuant[0]))

    if returnQuant[0] > 0:
        cur.execute("SELECT * FROM clients")
        clients = cur.fetchall()
        # for (full_name, phone, email) in cur:
        #     print("full_name: {}, phone: {}, email {}".format(full_name,phone,email))
        for row in cur:
            print(row[1])
        return render_template('clients.html', clients = clients)
    else:
        return render_template('addClients.html')
        cur.close()

#Add Clients
@app.route('/addClient', methods=['GET', 'POST'])
def addClients():
    return render_template('addClients.html')

#Add Client Process
#Structure adapted from: https://www.tutorialspoint.com/flask/flask_sqlite.htm
@app.route('/addClientProcess', methods=['POST', 'GET'])
def addClientProcess():
    if request.method == 'POST': #and form.validate():
        cur = db.cursor()
        msg = 'there was a serious error'
        try:
            print("maybe")
            full_name = request.form['first_name'] + " " + request.form['last_name']
            phone = request.form['phone']
            email = request.form['email']
            print "yay! full_name: %s" % full_name
            print "phone: %s" % phone
            print "email: %s" % email
            cur.execute("INSERT INTO clients (full_name, phone, email) VALUES (%s,%s,%s);", (full_name, phone, email))
            db.commit()
            msg = "Record successfully added"
        except:
            #cur.rollback()
            msg = "error in insert operation"
        finally:
            return render_template("addClientResult.html", msg=msg)
            cur.close()

#Single Client View
@app.route('/clients/<string:full_name>/')
def client(full_name):
    cur = db.cursor()
    clientId = (full_name,)

    #Get client information
    cur.execute("SELECT * FROM clients WHERE full_name = ?", clientId)
    clientInfo = cur.fetchone()
    #Render client information
    return render_template('article.html', article=article)
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
