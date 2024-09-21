# Docs

To run this spider:

```sh
scrapy startproject isbnchile # Create new Scrapy project
cd isbnchile; scrapy genspider books isbnchile # create spider 
scrapy crawl books -o books.json # Run the spider: 
```

```sh
scrapy shell <URL>
scrpy shell ; fetch(<URL>)
```
