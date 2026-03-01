import os
import subprocess
from jinja2 import *
from flask import Flask, render_template, redirect, request, url_for
from datetime import datetime
import webbrowser
from threading import Timer

phase_list = [
    ('parsed',
    r'reiko_acquisition\parsed_outputs'),
    
    ('evidence',
    r'reiko_acquisition\evidence_storage'),
]
file_data = []
for phase, location in phase_list:
    for folder, subfolders, files in os.walk(location):
        for file in files:
            file_data.append({
                "phase": phase,
                "folder": os.path.basename(folder),
                "file": file,
                "location": location
            })

app = Flask(__name__, template_folder=r'C:\Users\Stinky\Desktop\final_project\reiko_acquisition\web_app\templates')

@app.route("/")
def report():
    return render_template('report.html', file_data=file_data)

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
    port = 5000
    url = f"http://127.0.0.1:{port}/"
    Timer(1, lambda: webbrowser.open(url)).start()  # 1-second delay to let Flask start

    # Start Flask
    app.run(port=port, debug=True)



    


