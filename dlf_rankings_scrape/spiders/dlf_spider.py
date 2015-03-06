import scrapy
from dlf_rankings_scrape.items import DlfRanking

class DlfSpider(scrapy.Spider):
  name = "dlf"
  allowed_domains = ["http://dynastyleaguefootball.com/"]
  start_urls = ["http://dynastyleaguefootball.com/adpdata/2015-adp/?month=2"]

  def parse(self, response):
    overall_table_rows = response.xpath(
      "(//div[contains(@class, 'TabbedPanelsContent')]//table)[1]//tr")
    for row in overall_table_rows[1:]:
      data = row.xpath('td')
      ranking = DlfRanking()
      ranking['rank'] = data[0].xpath('text()')[0].extract()
      ranking['position'] = data[1].xpath('text()')[0].extract()
      ranking['player'] = data[2].xpath('a/text()')[0].extract()
      try:
        ranking['age'] = data[3].xpath('text()')[0].extract()
      except IndexError:
        ranking['age'] = 23 # Duron Carter's age is missing
      ranking['adp'] = data[4].xpath('text()')[0].extract()
      yield ranking

