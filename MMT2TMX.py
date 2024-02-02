#This script translates a TXT file using the machine translation engine ModernMT and writes the output directly to a TMX file. 
#This allows you to pretranslate texts using ModernMT and directly load them into a CAT tool.
#This allows you to use ModernMT with CAT tools that don't offer an integration for this engine.
#It requires that you get your own ModernMT API subscription at www.modernmt.com


import requests
import json
import modernmt
import pandas as pd
from modernmt import ModernMT
import xml.etree.ElementTree as ET
import xml.dom.minidom
import pandas as pd

# Define API key and file path - replace with your own values!
api_key = "YOUR_KEY"
file_path = r"SOURCE_FILE_PATH"
mmt = ModernMT(api_key)


# Function to clean text (if needed)
def clean_text(text):
    return text.strip().strip('"').rstrip(';')

# Read source file contents
with open(file_path, 'r') as file:
    file_contents = file.read()

# Convert source text into Python array
text_lines = [clean_text(row) for row in file_contents.split('\n') if row.strip()]

# Translate source text
translation = mmt.translate("en", "de", file_contents)
translation_raw = translation.translation

# Convert translation into array
translated_rows = [clean_text(row) for row in translation_raw.split('\n') if row.strip()]

# Create the root element of the TMX file
root = ET.Element('tmx', version='1.4')

# Create the body of the TMX file
body = ET.SubElement(root, 'body')

# Iterate over the text lines and their translations
for source, target in zip(text_lines, translated_rows):
    # Create a translation unit
    tu = ET.SubElement(body, 'tu')

    # Create translation elements for each language
    tuv_en = ET.SubElement(tu, 'tuv', lang='en-en')
    seg_en = ET.SubElement(tuv_en, 'seg')
    seg_en.text = source

    tuv_de = ET.SubElement(tu, 'tuv', lang='de-de')
    seg_de = ET.SubElement(tuv_de, 'seg')
    seg_de.text = target

# Convert the XML tree to a string
tmx_data = ET.tostring(root, encoding='unicode')

# Use minidom to pretty print the XML
dom = xml.dom.minidom.parseString(tmx_data)  # Parse the XML string
pretty_xml_as_string = dom.toprettyxml()

# Write to a file
tmx_file_path = 'translations.tmx'  # Specify your file path and name
with open(tmx_file_path, 'w', encoding='utf-8-sig') as file:
    file.write(pretty_xml_as_string)

print("TMX file created successfully.")
