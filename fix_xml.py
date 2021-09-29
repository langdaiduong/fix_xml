import os.path
from PyQt5.QtGui import QImage
import xml.etree.ElementTree as ET


forder = "./lhtm_train"
for file in os.listdir(forder):
    if file.endswith(".xml"):
        filePath = forder + "/" + file
        tree = ET.parse(filePath)
        root = tree.getroot()
        for country in root.findall('object'):
            name = country.find('name').text
            if name == "hand":
                root.remove(country)
        tree.write(forder + "/" + file)