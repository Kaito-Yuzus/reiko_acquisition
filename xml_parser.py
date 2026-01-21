import xml.etree.ElementTree as ET
import pandas as pd

xml_path = r'C:\Users\IKS.LAPTOP-AMM5L6TN\Desktop\final_project\reiko_acquisition\WifiConfigStore.xml'
tree = ET.parse(xml_path) 
root = tree.getroot()

data = []
for par_element in root.iter():
    for item in par_element:
        name = item.get('name')
        value = item.get('value')
        num = item.get('num')
        text = item.text
        if name is None: 
            continue

        if value is not None: 
            data.append({
            'Element' : par_element.tag,
            'Name': name,
            'Value': value, 
            })
            # Strip whitespaces within the .csv for better use
        elif num is not None:
            data.append({
            'Element' : par_element.tag,
            'Name': name,
            'Value': num, 
            })
        elif text is not None: 
            data.append({
            'Element' : par_element.tag,
            'Name': name,
            'Value': text, 
            })
        else: 
            data.append({
            'Element' : par_element.tag,
            'Name': name,
            'Value': 'Empty', 
            })
            print('This section is empty')

df = pd.DataFrame(data, columns=['Element', 'Name', 'Value'])
df.to_csv('output.csv', index=False)

for thing in data: 
    print(thing)