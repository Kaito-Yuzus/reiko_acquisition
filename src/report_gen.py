import os
import subprocess
from jinja2 import *
from flask import Flask, render_template, redirect, request, url_for
from datetime import datetime


parent_folder = r'C:\Users\Stinky\Desktop\final_project\reiko_acquisition\parsed_outputs'
file_data = []
for folder, subfolders, files in os.walk(parent_folder):
    for file in files:
        file_data.append({
            "phase": "parsed",
            "folder": os.path.basename(folder),
            "file": file,
            "location": folder
        })

locations = [
    r'C:\Users\Stinky\Desktop\final_project\reiko_acquisition\misc\requirements.txt', 
    r'C:\Users\Stinky\Desktop\final_project\reiko_acquisition\web_app\flask_start.py',
    r'C:\Users\Stinky\Desktop\final_project\reiko_acquisition\.gitignore'
]

app = Flask(__name__, template_folder=r'C:\Users\Stinky\Desktop\final_project\reiko_acquisition\web_app\templates')

@app.route("/")
def report():
    return render_template('report.html', locations=locations, file_data=file_data)

@app.route('/run-script')
def run_script():
    file_to_run = request.args.get('file')
    try:
        batch_path = r'reiko_acquisition\web_app\reiko_explorer.bat'
        # file = r'C:\Users\Stinky\Desktop\final_project\reiko_acquisition\web_app\flask_start.py'
        subprocess.Popen([batch_path, file_to_run], shell=True)
        return "Script started!"
    except Exception as e:
        return f"Error: {e}"












if __name__ == '__main__':
    app.run(debug=True)



    


