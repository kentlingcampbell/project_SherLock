import csv

def timeFilter(filename):

# OPEN FILE

    fields = []
    rows = []

    with open(filename, 'r') as csvfile:
        # create csv reader object
        csvreader = csv.reader(csvfile, delimiter='\t')

        # extract field name through first row
        fields = next(csvreader)

        # extract rows
        for row in csvreader:
            rows.append(row)

        # get total number of rows
        print("Total no. of input rows: %d" % (csvreader.line_num))

# FILTERING

        minTime = 1458086400000  # Should be 3/16/2016
        maxTime = 1459468800000  # Should be 4/1/2016

        filteredRows = []

        for idx, r in enumerate(rows):
            if (float(r[1]) > minTime) and (float(r[1]) < maxTime):
                filteredRows.append(r)

        # get total number of rows
        print("Total no. of filtered rows: %d" % (len(filteredRows)))

# WRITE FILE

        # name of output tsv file
        outfilename = "filteredData.tsv"

        # writing to tsv file
        with open(outfilename, 'w') as tsvfile:
            # creating a csv writer object
            csvwriter = csv.writer(tsvfile, delimiter='\t')

            # writing the fields
            csvwriter.writerow(fields)

            # writing the data rows
            csvwriter.writerows(filteredRows)


if __name__ == '__main__':
    timeFilter('../a_anon_T1.tsv')