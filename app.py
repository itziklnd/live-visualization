from flask import Flask, render_template, jsonify

app = Flask(__name__)

def load_data():
    completed = []
    incomplete = []
    with open('technologies.txt', 'r', encoding='utf-8') as f:
        data = f.read().split('#')
        if len(data) > 1:
            completed = data[1].strip().split()
        if len(data) > 0:
            incomplete = data[0].strip().split()
    return completed, incomplete

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/update-data')
def update_data():
    completed, incomplete = load_data()
    return jsonify({'completed': completed, 'incomplete': incomplete})

if __name__ == '__main__':
    app.run(debug=True)
