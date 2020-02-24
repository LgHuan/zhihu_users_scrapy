# -*- coding: utf-8 -*-
import json
import scrapy
from scrapy import Request
from zhihu.items import ZhihuItem
from zhihu.settings import DEFAULT_REQUEST_HEADERS


class ZhihuuserSpider(scrapy.Spider):
    name = 'zhihuuser'
    allowed_domains = ['www.zhihu.com']
    start_urls = 'https://www.zhihu.com/api/v4/members/{user}/activities?limit=7&session_id=1199334649136418816&after_id=1580538626&desktop=True'
    user_url='https://www.zhihu.com/api/v4/members/{user}/followers?include={include}&offset=0&limit=20'
    user_query='data[*].answer_count,articles_count,gender,follower_count,is_followed,is_following,badge[?(type=best_answerer)].topics'


    def start_requests(self):
        user='kehuan-90'
        #yield Request(self.start_urls.format(user=user),headers=DEFAULT_REQUEST_HEADERS,meta={'proxy':'47.112.222.108:8000'},callback=self.parse_user)
        yield Request(self.start_urls.format(user=user),headers=DEFAULT_REQUEST_HEADERS,callback=self.parse_user)
        yield Request (self.user_url.format (user=user, include=self.user_query), headers=DEFAULT_REQUEST_HEADERS,callback=self.parse)
        #yield Request(self.user_url.format(user=user,include=self.user_query),headers=DEFAULT_REQUEST_HEADERS,meta={'proxy':'47.112.222.108:8000'},callback=self.parse)

    def parse_user(self,response):
        result=json.loads(response.text)
        item=ZhihuItem()
        result_keys=result.get('data')[0].get('actor').keys()
        result_key=result.get('data')[0].get('actor')
        for field in item.fields:
            if field in result_keys:
                item[field]=result_key.get(field)
        yield item
        #yield Request(self.user_url.format(user=result.get('url_token'),include=self.user_query,offset=0,limit=20),meta={'proxy':'47.112.222.108:8000'},callback=self.parse)
        yield Request (self.user_url.format (user=result.get ('url_token'), include=self.user_query, offset=0, limit=20),callback=self.parse)

    def parse(self, response):
        results=json.loads(response.text)
        if 'data' in results.keys():
            for result in results.get('data'):
                yield Request(self.start_urls.format(user=result.get('url_token')),meta={'proxy':'47.112.222.108:8000'},callback=self.parse_user)
        if 'paging' in results.keys() and results.get('paging').get('is_end')==False:
            next_page=results.get('paging').get('next')
            #yield Request(next_page,meta={'proxy':'47.112.222.108:8000'},callback=self.parse)
            yield Request(next_page,callback=self.parse)