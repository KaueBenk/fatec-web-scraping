def get_links():
    # getting urls from links.txt
    archive = open('links.txt', 'r')
    links = []
    for line in archive:
        links.append(line.replace('\n', ''))
    archive.close()
    return links