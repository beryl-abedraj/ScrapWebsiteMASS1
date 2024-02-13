# WEB SCRAPING PROJECT TO SCRAPE A WEBSITE AND STORING THE DATA INTO MYSQL

from bs4 import BeautifulSoup                                                                                           # Importing BeautifulSoup
import requests                                                                                                         # Importing Requests
import mysql.connector                                                                                                  # Importing MySQL Connector

try:                                                                                                                    # Exceptional Block not to crash code
    db = mysql.connector.connect(host="localhost", user="root", password="root", database="python_db")                  # Creating path
    mycursor = db.cursor()
    def inserting(rankings,series_name,started_year,ratings,lead_actor_name):                                           # Creating function to Insert Data into RDBMS
        mycursor.execute("INSERT INTO series_list_25(rankings, series_name, started_year, ratings, lead_actor_name) VALUES (%s,%s,%s,%s,%s)",
                         (rankings, series_name, started_year, ratings, lead_actor_name))
        db.commit()


    link = requests.get("https://editorial.rottentomatoes.com/guide/rt25-critics-top-tv-shows-of-the-last-25-years-2/") # Declaring Website link
    soup = BeautifulSoup(link.text, "html.parser")                                                                      # Creating objects for BS4
    das = soup.body                                                                                                     # Declaring HTML Body part separately into another variable
    holder = das.find_all("div", attrs={"class": "row countdown-item"})                                                 # Finding all <div> tags with class = row countdown-item

    print("________________________________________________________________")
    for superior in holder:
        rank = superior.find("div", attrs={"class": "countdown-index"})                                                 # Finding <div> tag with class = countdown-index
        jason = superior.find("div", attrs={"class": "article_movie_title"})                                            # Finding <div> tag with class = article_movie_title
        name = jason.find("a")                                                                                          # Finding <a>
        year = jason.find("span", attrs={"class": "subtle start-year"})                                                 # Finding <span> tag with class = subtle start-year
        percent = jason.find("span", attrs={"class": "tMeterScore"})                                                    # Finding <div> tag with class = row countdown-item-details
        jimmy = superior.find("div", attrs={"class": "row countdown-item-details"})                                     # Finding <div> tag with class = row countdown-item-details
        josh = jimmy.find("div", attrs={"class": "info cast"})                                                          # Finding <div> tag with class = info cast
        actor = josh.find("a", attrs={"class": ""})                                                                     # Finding <a> tag with class = " "

        rankings = rank.string.replace("#", "")                                                                         # Using replacing method to replace '#' from string
        series_name = name.string
        started_year = year.string
        ratings = percent.string.replace("%", "")                                                                       # Using replacing method to replace '%' from string
        lead_actor_name = actor.string

        inserting(rankings, series_name, started_year, ratings, lead_actor_name)                                        # Passing the arguments into function to insert data into RDBMS

        print(rankings + "," + series_name + "," + started_year + "," + ratings + "," + lead_actor_name)                # Printing the Values
    print("________________________________________________________________")
except Exception as e:
    print(e)
