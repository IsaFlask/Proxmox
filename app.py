from flask import Flask, render_template, request, flash, redirect, session, url_for
import logging

from klas import Klas
from pool import Pool
from vituelecomputer import VirtuelComputer

logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)
app.secret_key = 'super secret key' # gebruik voor sessie.
app.config["TEMPLATES_AUTO_RELOAD"] = True # voor het herladen van templates als wijzigingen

klassen = []
h5c = Klas("H5C")
h5c.addComputer(VirtuelComputer("skvm313454", True, "win10"))
h5c.addComputer(VirtuelComputer("skvm313454_debian", True, "debian"))
h5c.addComputer(VirtuelComputer("skvm312344", False, "macos"))
h5c.addComputer(VirtuelComputer("skvm333322", False, "debian"))
h5c.addComputer(VirtuelComputer("skvm334435", True, "win10"))
klassen.append(h5c)

h5a = Klas("H5A")
h5a.addComputer(VirtuelComputer("skvm331111", True, "macos"))
klassen.append(h5a)

h5x = Klas("H5X")
h5x.addComputer(VirtuelComputer("skvm33ddd1111", True, "macos"))
h5x.addComputer(VirtuelComputer("skvm33ddd1111", True, "macos"))
h5x.addComputer(VirtuelComputer("skvm33ddd1111", True, "macos"))
h5x.addComputer(VirtuelComputer("skvm33ddd1111", True, "macos"))
h5x.addComputer(VirtuelComputer("skvm33ddd1111", True, "macos"))
h5x.addComputer(VirtuelComputer("skvm33ddd1111", True, "macos"))
klassen.append(h5x)


print("klassen aangemaakt")

pools = []
pool1 = Pool("Werkgroep avond")
pool1.addComputer(VirtuelComputer("skvm313454", True, "win10"))
pool1.addComputer(VirtuelComputer("skvm312344", False, "macos"))
pool1.addComputer(VirtuelComputer("skvm333322", False, "debian"))
pool1.addComputer(VirtuelComputer("skvm334435", True, "win10"))
pools.append(pool1)

pool2 = Pool("Leraren")
pool2.addComputer(VirtuelComputer("justin_bieber", True, "macos"))
pool2.addComputer(VirtuelComputer("Juice_Wrld", False, "debian"))
pool2.addComputer(VirtuelComputer("bill_gates", True, "macos"))
pool2.addComputer(VirtuelComputer("elon_musk", True, "win10"))
pools.append(pool2)
print("pools aangemaakt")

def update_comp_klas(comp):
    for k in klassen:
        for c in k.computers:
            if c.name == comp:
                c.Toggle()

def klas_aan_uit(klas, on):
    print(klas)
    print(on)
    for k in klassen:
        if k.name == klas:
            for c in k.computers:
                c.on = on

def update_comp_pool(comp):
    for p in pools:
        for c in p.computers:
            if c.name == comp:
                c.Toggle()

def pool_aan_uit(pool, on):
    for p in pools:
        if p.name == pool:
            for c in p.computers:
                c.on = on

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
        return render_template('overview.html', klassen=klassen, pools=pools)
    else:
        return redirect(url_for('index'))

@app.route('/klas', methods=('GET', 'POST'))
def klas():
    if 'logged_in' in session and session['logged_in'] == '1':
        if request.method == 'POST':
            aan = request.form.get('aan')     
            if aan == '1' or aan == '2':
                klas = request.form.get('klas')    
                klas_aan_uit(klas, aan == '1')
            pc = request.form.get('current_pc')   
            if pc != 'None':
                update_comp_klas(pc)

        return render_template('klas.html', klassen=klassen, pools=pools)
    else:
        return redirect(url_for('index'))

@app.route('/nieuwe-klas')
def nieuweklas():
    if 'logged_in' in session and session['logged_in'] == '1':
        return render_template('nieuweklas.html', klassen=klassen, pools=pools)
    else:
        return redirect(url_for('index'))

@app.route('/pool', methods=('GET', 'POST'))
def pool():
    if 'logged_in' in session and session['logged_in'] == '1':
        if request.method == 'POST':
            aan = request.form.get('aan')     
            if aan == '1' or aan == '2':
                pool = request.form.get('pool')   
                pool_aan_uit(pool, aan == '1')                
            pc = request.form.get('current_pc')   
            if pc != 'None':
                update_comp_pool(pc)

        return render_template('pool.html', klassen=klassen, pools=pools)
    else:
        return redirect(url_for('index'))

@app.route('/nieuwe-pool')
def nieuwepool():
    if 'logged_in' in session and session['logged_in'] == '1':
        return render_template('nieuwepool.html', klassen=klassen, pools=pools)
    else:
        return redirect(url_for('index'))

