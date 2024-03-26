from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    dob = request.form['dob']
    education = request.form['education']
    resume = request.files['resume']
    # Save the resume to a folder named 'resumes'
    resume.save('resumes/' + resume.filename)
    return render_template('success.html', name=name)

if __name__ == '__main__':
    app.run(debug=True)
