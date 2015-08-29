__author__ = 'zehavitc'
import xml.etree.ElementTree as ET


def parse_patterns_xml(path):
    tree = ET.parse(path)
    root = tree.getroot()
    patterns = []
    for child in root.iter('Pattern'):
        templates = []
        for message in child.iter('Message'):
            templates.append(message.text)
        responses = []
        for response in child.iter('Response'):
            responses.append(response.text)
        patterns.append([templates,responses])
    return patterns

# parse_patterns_xml(r'C:\Users\zehavitc\Desktop\patterns.xml')
