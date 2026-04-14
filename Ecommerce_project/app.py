import os
from flask import Flask, request, render_template

app= Flask(__name__, template_folder='templates')
products = [
    {id: 1, "name": 'laptop', 'price': '50000', 'image': 'laptop.jpg'},
    {id: 2, "name": "smartPhone", "price": '20000', 'image': 'phon.jpg'},
    {id: 3, 'name': 'Headsphones', 'price': '2,000', 'image': 'audio.jpg'}
]

@app.route('/')
def home():
    return render_template("index.html", items=products)

if __name__ == '__main__':
    app.run(debug=True)
