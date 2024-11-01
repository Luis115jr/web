from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/move_button')
def move_button():
    import random
    randomX = random.randint(-200, 200)
    randomY = random.randint(-200, 200)
    
    return jsonify({"x": randomX, "y": randomY})

if __name__ == '__main__':
    app.run(debug=True)
