from urllib.request import *
#import urllib2.urlopen
import ujson
import datetime

config = {}
exec(open("conf/default.conf").read(), config)


def pricing(list_instance_type):
    data = {}
    offer_codes_url = config["offer_codes_url"]
    try:
        request = urlopen(offer_codes_url)
    except urlib.error.URLError as e:
        print (e.reason)
    response = request.read()
    url_data = ujson.loads(response.decode())
    pricing_api_url = config["pricing_api_url"] \
        + url_data['offers']['AmazonEC2']['currentVersionUrl']
    try:
        request = urlopen(pricing_api_url)
    except urlib.error.URLError as e:
        print (e.reason)
    response = request.read()
    url_data = ujson.loads(response.decode())
    request.close()

    for testdata in url_data['products']:
        if ('productFamily' in url_data['products'][testdata].keys()
           and url_data['products'][testdata]
           ['productFamily'] == 'Compute Instance'
           and url_data['products'][testdata]
           ['attributes']['instanceType'] in list_instance_type
           and url_data['products'][testdata]
           ['attributes']['operatingSystem'] == config["operatingSystem"]
           and url_data['products'][testdata]
           ['attributes']['tenancy'] == config["tenancy"]
           and url_data['products'][testdata]
           ['attributes']['location'] == config["location"]):
            data[url_data['products'][testdata]
                 ['attributes']['instanceType']] = (url_data['terms']
                                                    ['OnDemand']
                                                    [testdata]
                                                    [testdata+'.JRTCKXETXF']
                                                    ['priceDimensions']
                                                    [testdata+'.JRTCKXETXF.6YS6EN2CT7']
                                                    ['pricePerUnit']['USD'])

    return data


def main():
    list_instance_type = ["m3.medium", "m1.small",
                          "m2.4xlarge", "c3.2xlarge",
                          "m1.large", "m3.xlarge",
                          "m3.large"]
    print (config)
    print (pricing(list_instance_type))

if __name__ == "__main__":
    main()
