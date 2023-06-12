from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('testing.html')

@app.route('/process_form', methods=['POST'])
def process_form():
    checked_values = request.form.getlist('checkboxes')
    return ', '.join(checked_values)

if __name__ == '__main__':
    app.run()
