# Web-Scraping-Challenge

For this project a Jupyter Notebook was created to scrape the following sites:

* NASA Mars News Site
  * Website was scraped to collect the latest News Title and Paragraph Text.
* JPL Nasa/Mars Space Images
  * Splinter was used to navigate the site and find the image url for the current Featured Mars Image. The url string was assigned to a variable called featured_image_url.
* Twitter/Mars Weather
  * Mars latest weather was scraped from the tweet page, and assigned to a variable called mars_weather.
* Space Facts/Mars
  * Pandas was used to scrape the table containing facts about the planet including Diameter, Mass, etc. Pandas was also used to convert the data to a HTML table string.
* USGS Astrogeology site
  * The site was scraped to obtain high resolution images for each of Mar's hemispheres.
  * A Python dictionary was used to store the data using the keys img_url and title.
  
 MongoDB with Flask templating was used to create a HTML page that displays all of the information that was scraped from the URLs above.
