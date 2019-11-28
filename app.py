from flask import Flask, request, redirect, url_for, render_template
from flask import session as login_session

from databases import *

app = Flask(__name__)
app.secret_key = "MY_SUPER_SECRET_KEY"

@app.route('/home.html')
def home():
	return render_template('home.html')

@app.route('/store.html')
def store():
	return render_template('store.html', products = products)
	#return render_template('store.html', products = products, add = add_to_cart(products[0]))

@app.route('/cart.html')
def cart():
	return render_template('cart.html')

@app.route('/')
def NewHome():
	return home()

@app.route('/add_to_cart/<int:productID>', methods = ['GET', 'POST'])
def add_to_cart(productID):
	add_to_cart(productID)
	return redirect(url_for('store'))

if __name__ == '__main__':
    app.run(debug=True)
