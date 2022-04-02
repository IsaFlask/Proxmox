from flask import Flask, render_template, request, flash, redirect, session, url_for
import logging

logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)
app.secret_key = 'super secret key' # gebruik voor sessie.
app.config["TEMPLATES_AUTO_RELOAD"] = True # voor het herladen van templates als wijzigingen

@app.route('/', methods=('GET', 'POST'))
def index():
    if request.method == 'POST':
        pincode = request.form.get('inputPincode')        
        print(pincode)
        if pincode != "1234": # Pincode opzoeken in databas normaal gesproken
            flash('Pincode is niet correct!')
        else: 
            session['logged_in'] = '1'
            return redirect(url_for('overview'))

    return render_template('index.html')

@app.route('/overview')
def overview():
    if 'logged_in' in session and session['logged_in'] == '1':
        return render_template('overview.html')
    else:
        return redirect(url_for('index'))

@app.route('/klas1')
def klas1():
    if 'logged_in' in session and session['logged_in'] == '1':
        return render_template('klas1.html')
    else:
        return redirect(url_for('index'))

@app.route('/klas2')
def klas2():
    if 'logged_in' in session and session['logged_in'] == '1':
        return render_template('klas2.html')
    else:
        return redirect(url_for('index'))

@app.route('/klas3')
def klas3():
    if 'logged_in' in session and session['logged_in'] == '1':
        return render_template('klas3.html')
    else:
        return redirect(url_for('index'))

@app.route('/klas4')
def klas4():
    if 'logged_in' in session and session['logged_in'] == '1':
        return render_template('klas4.html')
    else:
        return redirect(url_for('index'))
