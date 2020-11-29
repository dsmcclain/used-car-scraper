import scrapy

class TruecarSpider(scrapy.Spider):
  name = "truecar"

  def start_requests(self):
    urls = ['https://www.truecar.com/used-cars-for-sale/listings/hyundai/kona/',
    'https://www.truecar.com/used-cars-for-sale/listings/honda/hr-v/']

    for url in urls:
      yield scrapy.Request(url=url, callback=self.parse)

  def parse(self, response):
    
    all_listings = response.xpath('//div[@data-qa="Listings"]')

    for car in all_listings:
      make_model = car.css('div[data-test="vehicleListingCardTitle"] > div')
      year = make_model.css('span.vehicle-card-year::text').get()
      trim = make_model.css('div[data-test="vehicleCardTrim"]::text').get()
      model_raw = make_model.css('span.vehicle-header-make-model').get()
      model = model_raw[model_raw.find('>')+1:-7].replace('<!-- -->', '')

      car_data = {
        'url': 'http://truecar.com' + car.css('a::attr(href)').get(),
        'model': year + ' ' + model,
        'trim': trim,
        'color': car.css('div[data-test="cardContent"] > div > div.text-truncate::text').get(),
        'mileage': car.css('div[data-test="cardContent"] > div > div > div[data-test="vehicleMileage"]::text').get(),
        'price': car.css('h4::text').get(),
      }

      yield car_data
