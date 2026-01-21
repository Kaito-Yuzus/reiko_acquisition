import xml.etree.ElementTree as ET
#import pandas as pd

xml_path = r'C:\Users\IKS.LAPTOP-AMM5L6TN\Desktop\final_project\reiko_acquisition\WifiConfigStore.xml'
tree = ET.parse(xml_path) 
root = tree.getroot()

#parent = root.find('SoftAp')

for item in root:
    print(item.tag)


