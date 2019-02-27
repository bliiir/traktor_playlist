#!/usr/bin/env python3
# coding: utf-8

import pandas as pd
import lxml
import html5lib
import bs4

# Get filename and path from user
print('Filepath and name')
print('Example: /Users/rg/Dropbox/00 Privat/Audio/30_playlists_xml_etc/20181210.html')
filename =  input('please enter here: ')

# Extract path, title and extension from filename
file_path = filename.split('.')[0]
file_extension = filename.split('.')[-1]
file_name = file_path.split('/')[-1]

# Read html
l = pd.read_html(filename, header=0)

# Create a list of dataframes from the tables in the html file
df = l[0]


# Remove duplicates
df = df.drop_duplicates(subset='Title')

# Subset for export
df_export = df[['Title', 'Artist']]


# Export to csv
df_export.to_csv(f'{file_name}.csv', index=False)



