# MusicCulturalProject

>Student ID: 52211518
>
>Full Name: Junren Lai
>
>Render Url:https://cs551passignment.onrender.com

### Project introduction:

This project is to explore the relationship between the styles of many music artists and the popular elements of their times, and then analyze which style the public prefer.

### Data sources：

Data from http://millionsongdataset.com/pages/getting-dataset/,
The data is filtered here. 2000 data in the artist term table, 
2739 data in the artist mbtag, and 2017 data in the artists table are retained

## Technology selection:

Back-end: flask network framework, sqlite3 data storage

Template：jinjia2

### Project structure：

`dataset`: Store public data directory

​	`mbtag.csv`: 1997 data of mbtag and artist_id

​	`term.csv`: 2000 term and artist_id data

`features`: behave test

​	`driver`:  chrome driver

​		`chromedriver.exe`: chrome driver

​	`steps`: testing procedure

​		`customers.py` testing procedure

​	`customers.feature`: feature

​	`enviroment.py`: enviroment

`templates`: Directory where the web page template is stored

​	`index.html`: Website homepage file

​	`artist_term.html`: term page file

​	`artist_mbtag.html`: mbtag page file

`.gitignore`:gitIgnore uploaded files

`app.py`:Project entry file

`artist_style.db`:Database file

`setup_db.py`: Initialize site database script file

`requirements.txt`: Virtual environment dependency package file

`git-log.txt`:gitSubmit record documents

### Database design：

Table structure design of sqlite3 database used in this project：

`artist` table:Table for storing artist_id

​	artist_id: artist_id

`mbtag_artist`:Table storing the corresponding relationship between artist_id and mbtag

​	artist_id: artist_id

​	mbtag: mbtag

`term_artist`:A table storing the corresponding relationship between artist_id and term

​	artist_id: artist_id

​	term: term

### Function realization：

Visit the home page to get the data volume statistics of the three tables in the database, and jump to the mbtag statistics page or term statistics page

Visit the mbtag page to get the number and specific content of the de-duplicated mbtag in the database, and make statistics on the maximum associated amount of mgtag and the associated amount of artists

Visit the term page to get the number of terms in the database after duplication removal and the specific content, and make statistics on the maximum number of terms associated with artists

Provide a script to import csv data into the database


### Development process:

The first step in the development of this project is to find the right data to give me better inspiration, and combine my knowledge to form a complete website project.
I found a lot of data online, but none of them was what I wanted or didn't have much inspiration. Finally, I found this data set online.
Then I started to analyze the correlation between the data. Through analyzing the data, I found that the data in the two tables of artist term and artist mbtag in this dataset are related,
So I merged the data in the two tables, stored the merged data in the artist table, and designed three tables when designing the table structure of the database,
They are the artist table, the mbtag artist table, and the term artist table. The artist id field of the mbtag artist and term artist tables are foreign keys, pointing to the artist id field of the artist table.

Through a set up.py script file, the data in the csv file is imported into the database to provide initialization data for the website.

When designing the section of the website, I used the flask framework, and then used the jinja 2 template. The page layout adopted the style provided by bootstrap 4. I designed three sections, namely the artist section, the mbtag section, and the term section.

Through sqlite module and g control database connection, the database is queried, and then the queried data is transferred to the template, which then renders the data to the page.

In terms of data statistics of the artist section, the association query method is used to obtain the corresponding data and transfer it to the template for rendering data.

During the overall development process, git is used for version control. Each submission will record the content submitted and the submission time. This allows me to view my development progress at any time during the development process.

