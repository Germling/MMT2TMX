#This is a PY  file with a script to translate a source text in TXT format using the ModernMT API and then save the results to a TMX file that can be read by most professional translation tools

#!/usr/bin/env python
# coding: utf-8

import requests
import csv
import json
import modernmt
import pandas as pd
from modernmt import ModernMT

# Define API key and file path
api_key = "YOUR_API_KEY"
file_path = r"PATH_TO_YOUR_SOURCE_FILE"
csv_file_path = r"PATH_TO_YOUR_CSV_FILE"
mmt = ModernMT(api_key)

# Read source file contents
with open(file_path, 'r') as file:
    file_contents = file.read()

# Convert source text into Python array
text_lines = [row for row in file_contents.split('\n') if row.strip()]

print(text_lines)

# Translate source text
translation = mmt.translate("en", "de", file_contents)

translation_raw = translation.translation

# Convert translation into array
translated_rows = [row for row in translation_raw.split('\n') if row.strip()]

print(translated_rows)

# Convert array into Pandas dataframe
df = pd.DataFrame({'en-en': text_lines, 'de-de':translated_rows})
print(df)

def clean_text(text):
    # Strip leading and trailing whitespace, then strip surrounding quotes, then strip trailing semicolon
    return text.strip().strip('"').rstrip(';')

# Convert dataframe to CSV file
for column in df.columns:
    df[column] = df[column].apply(clean_text)

df.to_csv('translated_texts.csv', sep=';', index=False, encoding='utf-8-sig')

import xml.etree.ElementTree as ET
import xml.dom.minidom

# Create the root element of the TMX file
root = ET.Element('tmx', version='1.4')

# Create the body of the TMX file
body = ET.SubElement(root, 'body')

# Iterate over the DataFrame rows and add them to the TMX body
for index, row in df.iterrows():
    # Create a translation unit
    tu = ET.SubElement(body, 'tu')

    # Create translation elements for each language
    tuv_en = ET.SubElement(tu, 'tuv', lang='en-en')
    seg_en = ET.SubElement(tuv_en, 'seg')
    seg_en.text = row['en-en']

    tuv_de = ET.SubElement(tu, 'tuv', lang='de-de')
    seg_de = ET.SubElement(tuv_de, 'seg')
    seg_de.text = row['de-de']

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
