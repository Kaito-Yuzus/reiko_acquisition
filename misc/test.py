import os

# Set the parent folder
parent_folder = r'C:\Users\Stinky\Desktop\final_project\reiko_acquisition\parsed_outputs'
phase_name = os.path.basename(parent_folder)  # "parsed_outputs"

# Collect all files and their folders
file_data = []
for folder, subfolders, files in os.walk(parent_folder):
    for file in files:
        file_data.append({
            "phase": phase_name,
            "folder": os.path.basename(folder),
            "file": file,
            "location": folder
        })

# Build HTML content
html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Folder Report</title>
    <style>
        body {{ font-family: Arial, sans-serif; padding: 20px; }}
        table {{ border-collapse: collapse; width: 100%; }}
        th, td {{ border: 1px solid #ddd; padding: 8px; text-align: left; }}
        th {{ background-color: #4CAF50; color: white; }}
        tr:nth-child(even) {{ background-color: #f2f2f2; }}
        tr:hover {{ background-color: #ddd; }}
    </style>
</head>
<body>
    <h1>Folder Report</h1>
    <table>
        <tr>
            <th>Phase</th>
            <th>Folder</th>
            <th>File</th>
            <th>Location</th>
        </tr>
"""

# Add rows for each file
for item in file_data:
    html_content += f"""
        <tr>
            <td>{item['phase']}</td>
            <td>{item['folder']}</td>
            <td>{item['file']}</td>
            <td>{item['location']}</td>
        </tr>
    """

# Close HTML
html_content += """
    </table>
</body>
</html>
"""

# Save the HTML file
output_file = r'C:\Users\Stinky\Desktop\final_project\folder_report.html'
with open(output_file, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"Report generated: {output_file}")













# env = Environment(loader=FileSystemLoader(r'reiko_acquisition\web_app\templates'))
# template = env.get_template('report.html')

# output = template.render(locations=locations)

# with open(r'report_output.html', 'w') as f:
#     f.write(output)
