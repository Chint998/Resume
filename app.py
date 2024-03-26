from flask import Flask, render_template, request
import os

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
    
    # Create the 'resumes' directory if it doesn't exist
    if not os.path.exists('resumes'):
        os.makedirs('resumes')
    
    # Save the resume to the 'resumes' directory
    resume.save(os.path.join('resumes', resume.filename))
    
    return render_template('success.html', name=name)

if __name__ == '__main__':
    app.run(debug=True)
