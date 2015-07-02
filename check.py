import csv
import re
import os
import sys

pattern = re.compile('([A-PR-UWYZ]([A-HK-Y][0-9]([0-9]|[ABEHMNPRV-Y])?|[0-9]([0-9]|[A-HJKPSTUW])?)[0-9][ABD-HJLNP-UW-Z]{2})')

os.chdir('data')
postcode_files = os.listdir('.')
files_to_process = 0
for postcode_file in postcode_files:
    if postcode_file.endswith(".csv"):
        files_to_process += 1

# file_length = file_len('postcodes.txt')
# f = open('postcodes.txt')

print 'Checking postcodes...'

progress = 0

for postcode_file in postcode_files:
    if postcode_file.endswith(".csv"):
        with open(postcode_file, "rb") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',', quotechar='"')
            for csv_row in csv_reader:
                postcode = csv_row[0].replace(" ", "")

                if not re.match(pattern, postcode):
                    print ''
                    print 'Error: Postcode %s does not match!' % postcode
                    sys.exit(0)

    progress += 1
    percentage = ((progress / float(files_to_process)) * float(100))
    blocks = int(percentage / 5)
    if percentage > 100:
        percentage = 100
    sys.stdout.write("\rProgress: [%s] %.2f%%" % ('#' * blocks + '-' * (20 - blocks), percentage))
    sys.stdout.flush()

print ''
print 'Complete!'
