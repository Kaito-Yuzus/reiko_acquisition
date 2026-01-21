import xml.etree.ElementTree as ET
import pandas as pd

xml_path = r'C:\Users\IKS.LAPTOP-AMM5L6TN\Desktop\final_project\reiko_acquisition\WifiConfigStore.xml'
tree = ET.parse(xml_path) 
root = tree.getroot()

data = []
for par_element in root:
    for item in par_element:
        name = item.get('name')
        value = item.get('value')
        num = item.get('num')
        text = item.text
        if name is None: 
            continue


        if value is None: 
            data.append({
            'Element' : par_element.tag,
            'Name': name,
            'Value': text, 
            })

            # Decide How I will make num work
        if value num is None
            data.append({
            'Element' : par_element.tag,
            'Name': name,
            'Value': value, 
            })

df = pd.DataFrame(data, columns=['Element', 'Name', 'Value'])
df.to_csv('output.csv', index=False)

for thing in data: 
    print(thing)