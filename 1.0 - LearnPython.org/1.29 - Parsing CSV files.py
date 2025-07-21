#So CVS stands for 'comma seperated values', something I never knew!
#It's an easy format to export databases (commas being delimiters)
#Python can work with .csv files very easily 

import csv
#help(csv)

# R E A D I N G __ A N D __ P R I N T I N G __ A __ C S V

with open(r"C:\Users\ellio\Documents\Documents - Python\A beginners guide to Python\1.0 - LearnPython.org\1.29 - CSV sample files\2019.csv", 'r') as csvfile2019:
    csvscalper = csv.reader(csvfile2019)
    for row in csvfile2019:
        print(row)

#We can add csvreader.next() before the loop, as csvscaleper is an iterator
#This would then not print the column headers(names)


# W R I T I N G __ T O __ A __ C S V
headers = [["Name", "Medium", "Medium Usability", "Course Depth", "Course Pacing","Course Logic"],
           ["LearnPython.Org", 9, 8, 6, 6]]

newFileName = r"C:\Users\ellio\Documents\Documents - Python\A beginners guide to Python\1.0 - LearnPython.org\1.29 - CSV sample files\courseReview.csv"

with open(newFileName, 'w', newline = '') as newCSVFile: #added in the newline to remove the blank line you get
    csvwriter = csv.writer(newCSVFile)
    csvwriter.writerows(headers)

# I D E A __ T I M E 
#Open up folder location
#Look in here and cycle through the files, dates are 2015 to 2019
#Open them up one by one, and find the row where the country = "United Kingdom"
#When we have that row, add it as a new line to a list
#Write the list to a new file called "UK over time"

ukDatabase = []
folderLocation = r"C:\Users\ellio\Documents\Documents - Python\A beginners guide to Python\1.0 - LearnPython.org\1.29 - CSV sample files"

# This will store the first set of headers we find
chosen_headers = None

for year in range(2015, 2019):
    with open(f"{folderLocation}\\{year}.csv", 'r', encoding='utf-8') as currentYear:
        annualCSVReader = csv.reader(currentYear)
        headers = next(annualCSVReader)  # Read the first row (headers)

        if not chosen_headers:
            # Prepend 'Year' to the header row
            chosen_headers = ["Year"] + headers

        # Try to find the right column for 'Country' or similar
        for index, header in enumerate(headers):
            if header.strip().lower() in ["country", "country or region"]:
                country_col = index
                break
        else:
            continue  # Skip if country column not found

        for row in annualCSVReader:
            if row[country_col].strip() == "United Kingdom":
                ukDatabase.append([year] + row)  # Prepend the year

# Write to new file
CSVFile = f"{folderLocation}\\UKDB.csv"
with open(CSVFile, 'w', newline='', encoding='utf-8') as newCSVFile:
    csvwriter = csv.writer(newCSVFile)
    csvwriter.writerow(chosen_headers)  # Write the header once
    csvwriter.writerows(ukDatabase)
        

#Right so after all that there is a csv.DictWriter and DictReader

