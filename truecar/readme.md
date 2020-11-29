**Updating the User Agent**

Open `truecar/settings.py` and edit `USER_AGENT = 'xyz'` to match your browser specifications.

**Adding/Changing URLs**

Open `truecar/spiders/truecar_spider.py` and modify the `urls` array to contain all the listings you would like to scrape. Truecar accepts query params in the url so you can play around on the website to apply whatever filters you would like and paste the url with the params into this array.

**Running the Scraper**

Run the following command, where `truecar.csv` is the name of the output file you would like to generate. You can also choose a `.json` extension and scrapy will output in json.

```
scrapy crawl truecar -o truecar.csv
```
