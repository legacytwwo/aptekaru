import scrapy
import requests
import json
import os

class AptekaRu(scrapy.Spider):
  name = 'aptekaru'
  api_url = 'https://api.apteka.ru/'

  def __init__(self, city='5e57a3bd752ac70001593b7b', **kwargs):
    self.city = city
    self.http = requests.Session()
    self.http.proxies = {'https': os.environ.get("PROXY")}

  def start_requests(self):
    response = self.http.get(
      timeout=15,
      url=self.api_url+'catalog/allitems',
    )
    urls = []
    if response.ok:
      data = response.text
      data = json.loads(data, strict=False)
      for x in data['goodGroup']:
        for x2 in x['subGroup']:
          urls.append(str(x['url']+'/'+x2['url']))
    for x in urls:
      url = x
      page = 0
      page_size = 50
      yield scrapy.Request(
        callback = self.parse,
        cb_kwargs = dict(url=url),
        meta = {'proxy': os.environ.get("PROXY")},
        url = f'{self.api_url}Search/GoodGroupUrl?pageSize={str(page_size)}&page={str(page)}&goodGroupUrl={url}&cityId={str(self.city)}'
      )

  def parse(self, response, url):
    data = response.text
    data = json.loads(data, strict=False)
    if data.get('result'):
      page = data['page'] + 1
      page_size = data['pageSize']
      for x in data['result']:
        yield scrapy.Request(
          callback = self.parse_good,
          meta = {'proxy': os.environ.get("PROXY")},
          url = f'{self.api_url}Item/GroupInfo?itemGroupId={x["id"]}&cityId={str(self.city)}'
        )
      if data['totalCount'] > (page * page_size):
        yield scrapy.Request(
          callback = self.parse,
          cb_kwargs = dict(url=url),
          meta = {'proxy': os.environ.get("PROXY")},
          url = f'{self.api_url}Search/GoodGroupUrl?pageSize={str(page_size)}&page={str(page)}&goodGroupUrl={url}&cityId={str(self.city)}',
        )

  def parse_good(self, response):
    data = response.text
    data = json.loads(data, strict=False)
    if data.get('groupItems'):
      for x in data['groupItems']:
        for x2 in x['itemInfos']:
          result = {
            'id': x2['id'],
            'name': x2['name'],
            'price': x2['price'],
            'manufacturer': x2['vendor']
          }
          yield result