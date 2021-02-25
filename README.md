# Web Scraping with Python

When FATEC releases the classification list they remove it after some weeks, so if you want to know the grade needed to enter the course you need to save it on your computer.

So I made this script to facilitate saving the classification list of my interest courses.

## How to use

Open links.txt and paste the links of the courses you want to save the classification list, line by line with an enter at the end of each link, like in the following model:

```url
https://www.vestibularfatec.com.br/classificacao/lista.asp?codfatec=45&codescolacurso=1977&o=1
https://www.vestibularfatec.com.br/classificacao/lista.asp?codfatec=45&codescolacurso=1978&o=1
https://www.vestibularfatec.com.br/classificacao/lista.asp?codfatec=45&codescolacurso=2237&o=1
```

Run "start.py" and watch your .csv files being created inside folders named with the school's name.

## Dependencies

* BeautifulSoup
* csv
* os
* requests
* time
