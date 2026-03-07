import os
import subprocess
from jinja2 import *
from flask import Flask, render_template, redirect, request, url_for
from datetime import datetime
import webbrowser
from threading import Timer

def rend_report():
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

    app = Flask(__name__, template_folder=r'C:\Users\IKS.LAPTOP-AMM5L6TN\Desktop\final_project\reiko_acquisition\web_app\templates')

    @app.route("/")
    def report():
        return render_template('report.html', file_data=file_data)

    @app.route('/run-script')
    def run_script():
        file_to_run = request.args.get('file')
        try:
            batch_path = r'reiko_acquisition\web_app\reiko_explorer.bat'
            # file = r'C:\Users\Stinky\Desktop\final_project\reiko_acquisition\web_app\flask_start.py'
            #File explorer link
            subprocess.Popen([batch_path, file_to_run], shell=True)
            return "Script started!"
        except Exception as e:
            return f"Error: {e}"
        
    port = 5000
    url = f"http://127.0.0.1:{port}/"
    Timer(1, lambda: webbrowser.open(url)).start()  # 1-second to start flask app need before to open site
    # Start Flask
    #Debugs Makes it run twice with previous code
    #Use reloader restarts the server when the code is saved
    #debugger runs the site in the browser and shows errors in the terminal
    app.run(port=port, debug=False, use_reloader=False)


if __name__ == '__main__':
    rend_report()