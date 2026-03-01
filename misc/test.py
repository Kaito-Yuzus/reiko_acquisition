import os
from datetime import datetime

# Folder you want to scan
folder_path = r"C:\Users\Stinky\Desktop\final_project\reiko_acquisition\parsed_outputs"  # <-- Change this

output_file = "folder_report.html"

rows = ""

for root, dirs, files in os.walk(folder_path):
    for file in files:
        file_path = os.path.join(root, file)
        size = os.path.getsize(file_path)
        modified_time = os.path.getmtime(file_path)
        modified_time = datetime.fromtimestamp(modified_time)

        rows += f"""
        <tr>
            <td>{file}</td>
            <td>{file_path}</td>
            <td>{size / 1024:.2f} KB</td
            <td>{modified_time}</td>
        </tr>
        """

html_content = f"""
<!DOCTYPE html>
<html>
<head>
    <title>Folder Report</title>
    <style>
        body {{ font-family: Arial; background-color: #f4f4f4; }}
        table {{ border-collapse: collapse; width: 100%; background: white; }}
        th, td {{ border: 1px solid #ddd; padding: 8px; }}
        th {{ background-color: #4CAF50; color: white; }}
        tr:nth-child(even) {{ background-color: #f2f2f2; }}
    </style>
</head>
<body>
    <h2>Folder Report: {folder_path}</h2>
    <table>
        <tr>
            <th>File Name</th>
            <th>Full Path</th>
            <th>Size</th>
            <th>Last Modified</th>
        </tr>
        {rows}
    </table>
</body>
</html>
"""

with open(output_file, "w", encoding="utf-8") as f:
    f.write(html_content)

print("HTML report generated:", output_file)