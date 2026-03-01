# app.py
from flask import Flask, request, render_template
import subprocess
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    locations = ['file1.txt', 'file2.txt']  # Example
    year = datetime.now().year
    return render_template('base.html', locations=locations, year=year)

@app.route('/run_bat', methods=['POST'])
def run_bat():
    filename = request.form.get('file')
    # Sanitize input to avoid security issues
    allowed_files = ['file1.txt', 'file2.txt']
    if filename not in allowed_files:
        return "Invalid file", 400

    try:
        # Run the .bat file with the filename as an argument
        result = subprocess.run(
            ['C:\\path\\to\\reiko_explorer.bat', filename],
            capture_output=True, text=True, check=True
        )
        # Show the output in the browser
        return f"<pre>{result.stdout}</pre>"
    except subprocess.CalledProcessError as e:
        return f"Error running script:\n<pre>{e.stderr}</pre>"

if __name__ == '__main__':
    app.run(debug=True)