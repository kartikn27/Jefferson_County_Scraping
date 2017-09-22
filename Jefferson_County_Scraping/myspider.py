import scrapy
import csv
import os
from scrapy.utils.response import open_in_browser

file_exists = os.path.isfile('jefferson.csv')
if file_exists:
    os.remove('jefferson.csv')

class BlogSpider(scrapy.Spider):
    name = 'myspider'

    def __init__(self, city='all', url='http://jefferson.sdgnys.com/search.aspx', sessionID='', *args, **kwargs):
        super(BlogSpider, self).__init__(*args, **kwargs)
        self.city = city
        self.url = url
        self.sessionID = sessionID

    def start_requests(self):
        return [scrapy.Request(
            url=self.url,
            # cookies={'ASP.NET_SessionId': self.sessionID,
            #          'TestCookie': 'test', 'LastSessID': self.sessionID,
            #          'HasAgreedToDisclaimer': 'True',
            #          'pubAccID': '20'
            #          },
            cookies={'ASP.NET_SessionId':'dd3t30553oko1mnlsyomky55',
                     'TestCookie': 'test', 'LastSessID': 'dd3t30553oko1mnlsyomky55',
                     'IMOSearchMode':'basic',
                     'HasAgreedToDisclaimer': 'True',
                     'pubAccID': '20'
                     },
            callback=self.parse
        )]

    def parse(self, response):
        # open_in_browser(response)
        return scrapy.FormRequest(self.url,
                                  formdata={'__EVENTTARGET': '',
                                            '__EVENTARGUMENT': '',
                                            '__VIEWSTATE': '/wEPDwUJNDU1Nzg0NzYzD2QWAgIDD2QWEgICDw8WAh4EVGV4dAUXSmVmZmVyc29uIENvdW50eSBTZWFyY2hkZAIEDxBkDxYXZgIBAgICAwIEAgUCBgIHAggCCQIKAgsCDAINAg4CDwIQAhECEgITAhQCFQIWFhcQBRJBbGwgTXVuaWNpcGFsaXRpZXMFA2FsbGcQBQVBZGFtcwUEMjIyMGcQBQpBbGV4YW5kcmlhBQQyMjIyZxAFB0FudHdlcnAFBDIyMjRnEAUKQnJvd252aWxsZQUEMjIyNmcQBQxDYXBlIFZpbmNlbnQFBDIyMjhnEAUIQ2hhbXBpb24FBDIyMzBnEAUHQ2xheXRvbgUEMjIzMmcQBQlFbGxpc2J1cmcFBDIyMzRnEAUJSGVuZGVyc29uBQQyMjM2ZxAFCkhvdW5zZmllbGQFBDIyMzhnEAUGTGUgUmF5BQQyMjQwZxAFCExvcnJhaW5lBQQyMjQyZxAFBEx5bWUFBDIyNDRnEAUHT3JsZWFucwUEMjI0NmcQBQdQYW1lbGlhBQQyMjQ4ZxAFDFBoaWxhZGVscGhpYQUEMjI1MGcQBQZSb2RtYW4FBDIyNTJnEAUHUnV0bGFuZAUEMjI1NGcQBQdUaGVyZXNhBQQyMjU2ZxAFCVdhdGVydG93bgUEMjI1OGcQBQVXaWxuYQUEMjI2MGcQBQVXb3J0aAUEMjI2MmdkZAIPDxBkDxYDZgIBAgIWAxAFDUFueSBTaXRlIFR5cGUFA2FueWcQBQtSZXNpZGVudGlhbAUDcmVzZxAFCkNvbW1lcmNpYWwFA2NvbWdkZAISDw8WAh8ABRlTd2l0Y2ggdG8gQWR2YW5jZWQgU2VhcmNoZGQCEw8WAh4HVmlzaWJsZWhkAhQPDxYCHwFoZGQCFg8PFgIfAAUFMTcuMDhkZAIXDw8WBB8ABQowNy8xMS8yMDE3HgdUb29sVGlwBRhWNEV4dHJhY3QgVmVyc2lvbjogMTYuMTJkZAIYD2QWAgIBDw8WAh8ABYcGPHA+V2VsY29tZSB0byBKZWZmZXJzb24gQ291bnR5IFJlYWwgUHJvcGVydHkgVGF4IFNlcnZpY2VzIGFzc2Vzc21lbnQgaW5mb3JtYXRpb24gcGFnZS4gICAgVGhpcyBzaXRlIHdpbGwgYWxsb3cgdXNlcnMgdG8gYWNjZXNzIHRoZSBpbmZvcm1hdGlvbiBjb21tb25seSByZXF1ZXN0ZWQgb24gcGFyY2VscyBpbiBKZWZmZXJzb24gQ291bnR5IG91dHNpZGUgdGhlIENpdHkgb2YgV2F0ZXJ0b3duLiAgIFRvIHZpZXcgcGFyY2VsIGluZm9ybWF0aW9uIGZvciB0aGUgQ2l0eSBvZiBXYXRlcnRvd24gcGxlYXNlIGdvIHRvIGh0dHA6Ly93d3cud2F0ZXJ0b3duLW55Lmdvdi9pbW8vLjwvcD4NCjxwPiZuYnNwOzwvcD4NCjxwPkN1cnJlbnQgdGF4IGluZm9ybWF0aW9uIGFuZCByYXRlcyBhcmUgYXZhaWxhYmxlIGJ5IGNsaWNraW5nIG9uIFRheCBJbmZvIHdoZW4gdmlld2luZyBhIHNwZWNpZmljIHBhcmNlbDwvcD4NCjxwPiZuYnNwOzwvcD4NCjxwPlRoZSB0YXggY2FsY3VsYXRvciB3aWxsIG5vdCB3b3JrIGZvciB0b3ducyBwZXJmb3JtaW5nIGEgcmV2YWx1YXRpb24uICZuYnNwO0ZvciAyMDE3IHRoZSBUb3ducyBwZXJmb3JtaW5nIGEgcmV2YWx1YXRpb24gYXJlIExvcnJhaW5lIGFuZCBSb2RtYW4uICZuYnNwOyBJZiB5b3UgaGF2ZSBzcGVjaWZpYyBxdWVzdGlvbnMgYWJvdXQgdGhlIHJldmFsdWF0aW9ucyBwbGVhc2UgY2FsbCB5b3VyIEFzc2Vzc29yLjwvcD4NCjxwPiZuYnNwOzwvcD4NCjxwPjIwMTcgRmluYWwgUm9sbCB2YWx1ZXMgYXJlIG5vdyBhdmFpbGFibGUuPC9wPmRkZBA8N1DPeA3rz2J6d7Zpu+3XFF6g',
                                            '__VIEWSTATEGENERATOR': 'BBBC20B8',
                                            '__EVENTVALIDATION': '/wEWHwLN5KG6BAKJlJfbBQKK29iCCwKK24DLDQKK2+j1DgKK29C/DwKK2/i7BQKtssf3AQKtsq+gAgKtspfqBAKtsv+UBQKtsueQCwLAiOXsBwLAiM2WCALAiLXfCgLAiJ2JCwLAiIWFAQL754PBDQL75+uLDgL759O1DwL757v+AQL756P6BwKe/qG2AgKe/ongBALpzrOKBQKHle2bDgKFn5PZAQKKh+66AwL9t8a4BgKln/PuCgK09sWVBYzdEKpwnd681u9PEWJLs1zXYUUN',
                                            'ddlMunic': self.city,
                                            'txtTaxMapNum': '',
                                            'txtLastOwner': '',
                                            'txtFirstOwner': '',
                                            'txtStreetNum': '',
                                            'txtStreetName': '',
                                            'btnSearch': 'Search',
                                            'hiddenInputToUpdateATBuffer_CommonToolkitScripts': '1'},
                                  callback=self.form_submit)

    def form_submit(self, response2):
        # open_in_browser(response2)
        for row in response2.css('.reportTable tr:not(.historic)'):
            counter = 0
            userData = {}
            for td in row.css('td'):
                counter += 1
                userData[counter] = td.css('::text').extract()
                #print("DATA   ", userData[counter])

                if counter == 2:
                    tax_link = td.css('a ::attr(href)').extract_first()


            if tax_link:
                #yield scrapy.Request(response2.urljoin(tax_link), meta=userData, callback=self.houseCost)
                #report_link = td.css('a ::attr(href)').extract_first()
                #return scrapy.Request(url=tax_link, callback=self.prop_detail)]
                yield scrapy.Request(url='http://jefferson.sdgnys.com/'+tax_link, callback=self.prop_detail)


        next_page = response2.css('#lnkNextPage ::attr(href)').extract_first()
        if next_page:
            yield scrapy.Request(response2.urljoin(next_page), callback=self.form_submit)

    def houseCost(self, response):
        userData = response.meta
        # yield {
        #     'town': userData[1] if len(userData)>1 else '',
        #     'name': userData[3] if len(userData)>3 else '',
        #     'streetnum': userData[4] if len(userData)>4 else '',
        #     'streetname': userData[5] if len(userData)>5 else '',
        #     'fullMarketValue': response.css('#lblFullMarketValue ::text').extract_first(),
        #     'landAssessment': response.css('#lblLandAssess ::text').extract_first(),
        #     'totalAssessment': response.css('#lblTotalAssess ::text').extract_first(),
        #     'propertyClass': response.css('#lblSitePropClass ::text').extract_first(),
        #     'site': response.css('#lblSite ::text').extract_first(),
        #     'school': response.css('#lblSchoolDist ::text').extract_first(),
        #     'neighborhood': response.css('#lblNeighborhood ::text').extract_first()
        #}

    def prop_detail(self, response):
        #report_link = response.css('#btnReport').extract_first()
        owner_code = response.css('#lblOwnerShipCode ::text').extract_first()
        response = str(response)
        if 'propdetail' in response:
            response = response.replace('<', '').replace('>', '').replace('200 ', '')
            response_param = response.split('?')[1]
            swis = response_param.split('&')[0].split('=')[1]
            print_key = response_param.split('&')[1].split('=')[1]
            report_url = 'http://jefferson.sdgnys.com/report.aspx?'
            report_url_new = report_url + 'file=&swiscode='+swis+'&printkey='+print_key+'&sitetype=res&siteNum=1'
            #print('report_url_new ', report_url_new)
            request = scrapy.Request(url=report_url_new, callback=self.report)
            request.meta['owner_code'] = owner_code
            #yield scrapy.Request(url=report_url_new, callback=self.report,kwargs={'owner code':owner_code})
            yield request

    def report(self, response):

        response = response.replace(body=response.body.replace(b'<br>', b' ,'))
        h_address = response.css('#lblReportTitle ::text').extract_first()
        ownership_code = response.meta['owner_code']
        print("OWNER CODE %%%%%%*********(((((((((()))))))))))))) ", ownership_code)
        swis = response.css('#lblSwis ::text').extract_first()
        owner_info=response.css('.owner_info ::text').extract_first()
        site= response.css('#lblSite ::text').extract_first()
        nieghborhood = response.css('#lblNeighborhoodCode ::text').extract_first()
        land_assessment = response.css('#lblLandAssessment ::text').extract_first()
        total_assessment = response.css('#lblTotalAssessment ::text').extract_first()
        full_market_value = response.css('#lblFullMarketValue ::text').extract_first()
        bedrooms=response.css('#lblBedrooms ::text').extract_first()
        total_acreage=response.css('#lblTotalAcreage ::text').extract_first()
        living_area=response.css('#lblLivingArea ::text').extract_first()
        second_story_area = response.css('#lblSecondStoryArea ::text').extract_first()
        building_style = response.css('#lblBuildingStyle ::text').extract_first()
        porch_type = response.css('#lblPorchType ::text').extract_first()
        porch_area = response.css('#lblPorchArea ::text').extract_first()
        overall_condition = response.css('#lblOverallCondition ::text').extract_first()
        overall_grade = response.css('#lblOverallGrade ::text').extract_first()
        sewer_type = response.css('#lblRSewerType ::text').extract_first()
        r_utilities = response.css('#lblRUtilities ::text').extract_first()
        water_supply = response.css('#lblRWaterSupply ::text').extract_first()
        print("h_add ", h_address)
        print ("OwnerShipCode",ownership_code)
        print("SWIS", swis)
        print("site ", site)
        print("nieghborhood ", nieghborhood)
        print("land_assessment ", land_assessment)
        print("total_assessment ", total_assessment)
        print("full_market_value ", full_market_value)
        print("bedrooms ", bedrooms)
        print("total_acreage ", total_acreage)
        print("owner_info ", owner_info)
        print("living_area",living_area)
        print("second_story_area",second_story_area)
        print("building_style",building_style)
        print("porch_type",porch_type)
        print("porch_area",porch_area)
        print("overall_condition",overall_condition)
        print("overall_grade",overall_grade)
        print("sewer_type",sewer_type)
        print("r_utilities",r_utilities)
        print("water_supply",water_supply)




        #myfile = open("Informationen.csv", "a")
        #writer = csv.writer(myfile, delimiter=',')
        # #writer.writerows(zip(owner_info.encode(),land_assessment.encode(),total_assessment,full_market_value,bathrooms,bedrooms,total_acreage))
        # writer.writerows(zip(owner_info,land_assessment))

        file_exists = os.path.isfile('jefferson.csv')
        with open('jefferson.csv', 'a') as csvfile:
            headers = ['h_address','SWIS','site','ownership_code','owner_info', 'land_assessment', 'total_assessment', 'total_acerage', 'full_market_value', 'bathrooms', 'bedrooms','living area','SecondStoryArea','BuildingStyle','PorchType','PorchArea','OverallCondition','OverallGrade','SewerType','Utilities','WaterSupply']
            writer = csv.DictWriter(csvfile, delimiter=',', lineterminator='\n', fieldnames=headers)

            if not file_exists:
                writer.writeheader()  # file doesn't exist yet, write a header

        with open('jefferson.csv', 'a') as csvfile:
            filewriter = csv.writer(csvfile, delimiter=',')
            filewriter.writerow([h_address,swis,site,ownership_code,owner_info, land_assessment, total_assessment, total_acreage, full_market_value, bedrooms,living_area,second_story_area,building_style,porch_type,porch_area,overall_condition,overall_grade,sewer_type, r_utilities, water_supply])




