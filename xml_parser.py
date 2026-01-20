import xml.etree.ElementTree as ET
import pandas as pd

xml_path = r'C:\Users\IKS.LAPTOP-AMM5L6TN\Desktop\final_project\reiko_acquisition\WifiConfigStoreSoftAp.xml'
tree = ET.parse(xml_path) 
root = tree.getroot()
parent = root.find('SoftAp')

data = []
headers = []

for item in parent: 
    name = item.get('name')
    value = item.get('value')

    if name is not None:

        headers.append(name)
        if item.text is not None:
            data.append(item.text)

        if value is not None: 
            data.append(value)

df = pd.DataFrame(data, columns=headers)
df.to_csv('output.csv', index=False)
print('Complete')
del df 
exit