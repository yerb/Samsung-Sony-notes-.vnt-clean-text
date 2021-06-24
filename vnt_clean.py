# Extract legacy Samsung notes with dates from .vnt files (notes export format)
import glob
import re

read_files = glob.glob("*.vnt")

print('Merging files...\n', read_files)

# Merge all .vnt files into one
with open("combined.txt", "wb") as outfile:
    for f in read_files:
        with open(f, "rb") as infile:
            outfile.write(infile.read())
# Read merged file
with open("combined.txt", 'r') as f:
    content = f.read()

# Clean the file to extract notes with dates
# Regex used is found here https://regex101.com/r/ufowNu/1/
# BEGIN:VNOTE[\S\s]+?PRINTABLE:([\S\s]+?)LAST-MODIFIED[\S\s]+?END:VNOTE

content_new = re.sub('BEGIN:VNOTE[\S\s]+?PRINTABLE:([\S\s]+?)D(CREATED:[\S\s]+?)T[\S\s]+?LAST-MODIFIED[\S\s]+?END:VNOTE', r'\2\n\1\n----\n', content, flags = re.M)

print(content_new)

# Write final output to file
output_file = input('Please enter output file name:\n')
with open(output_file, 'w') as f:
    f.write(content_new)
