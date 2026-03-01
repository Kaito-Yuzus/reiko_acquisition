env = Environment(loader=FileSystemLoader(r'reiko_acquisition\web_app\templates'))
template = env.get_template('report.html')

output = template.render(locations=locations)

with open(r'report_output.html', 'w') as f:
    f.write(output)
