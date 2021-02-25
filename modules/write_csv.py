from csv import writer, QUOTE_ALL

def write_csv (table_rows, archive, max_lines):
    # variables
    csv_lines = 0

    # writing to csv file
    for tr in table_rows:
        td = tr.find_all(["th", "td"])
        row = [i.text for i in td]
        wr = writer(archive, quoting = QUOTE_ALL)
        wr.writerow(row)
        csv_lines += 1
        if csv_lines == max_lines:
            break
