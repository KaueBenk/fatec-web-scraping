from modules.create_directory import create_directory
from modules.get_html_from_url import get_html_from_url
from modules.get_links import get_links
from modules.write_csv import write_csv

# settings
max_lines = 60  # define te maximum number of lines in csv file

links = get_links()

# variables
prevent_many_folders = 0
# in Brazil this is called gambiarra or technical temporary permanent adjust.
# Without this, script create a folder inside a folder inside a folder...
links_index = 0
max_lines += 1

# loop
while True:
    # getting html
    url = links[links_index]
    links_index += 1
    html = get_html_from_url(url)

    # getting course and school
    school = html.find_all('h4')
    school = school[1]
    course = html.find('h5')

    # formatting course and school
    school = str(school)[4:-5].title()
    course = str(course)[4:-5].title()

    # getting table_content
    table = html.find(
        "table", attrs={'class': 'table table-bordered table-striped'})
    table_rows = table.find_all("tr")

    # creating directory and csv file if they doesn't exists
    if prevent_many_folders == 0:
        create_directory(school)
        prevent_many_folders = 1
    archive = open(f'{course}.csv', 'x')

    # writing to csv file
    write_csv(table_rows, archive, max_lines)
