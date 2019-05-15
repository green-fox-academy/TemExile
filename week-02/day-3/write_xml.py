import json
import xml.etree.ElementTree as et


def wt_xml(file1, file2):
    with open(file1, encoding = 'utf-8', mode = 'r') as a:
        b = json.load(a)
    root = et.Element('Flowers')
    for lines in b:
        flower = et.SubElement(root, 'flower')
        for key, value in lines.items():
            et.SubElement(flower, key).text = str(value)
    output = et.ElementTree(root)
    output.write(open(file2, 'w'), encoding = 'unicode')

wt_xml('flowers.json', 'flowers.xml')
