#Weather forecast from yr.no, delivered by the Norwegian Meteorological #Institute and the NRK.
#
#During development it is advised to store a local cache of the weather data, #as yr.no provides this service for free, conditioned you keep query frequency #to a minimum.
#
#
#2014 martin.hagerup(at)gmail.com

import urllib.request
import xml.etree.ElementTree as etree
"""
This module provides a simple library to parse weather forecast data from Yr.no's free forecast service.
"""
class PyYrno:
    def __init__(self, location, lang):
        """

        Keyword arguments:
        location -- format "Country/County/Municipality/City"
        lang -- "en": english, "no": norwegian bokmål, "nn": nynorsk

        Example:

                PyYrno("Norway/Hordaland/Bergen/Bergen/", "no")
                -- forecast for Bergen in norwegian.
        """

        yr_feed = "http://www.yr.no/"
        yr_feed_end = "/forecast.xml"
        yr_langs = {"no" : "sted/", "nn" : "stad/", "en" : "place/"}
        self.yr_url = yr_feed+yr_langs[lang]+location+yr_feed_end
        self.forecast = self.fetch_forecast(self.yr_url)

    def update(self):
        """Fetch updated forecast."""
        self.forecast = self.fetch_forecast(self.yr_url)

    def fetch_forecast(self, url):
        """Returns the forecast in a map structure

        Parsing the xml weather data under <forecast><tabular>, passing a list of all the elements and values for each item into parse_data().
        """

        #tree = etree.parse(urllib.request.urlopen(url)) #Get from feed
        tree = etree.parse("forecast.xml") #Local test XML
        root = tree.getroot()
        forecasts = []
        #Parses the first time element and its children.
        for time in root[5][1].iter("time"):
            forecast_message = []
            forecast_message.append(time.attrib)
            #get the child elements in time parent
            for child in time:
                forecast_message.append(child.attrib)
            forecasts.append(forecast_message)

        return self.parse_data(forecasts)

    def parse_data(self, forecasts):
        """Returns the forecast in a map structure.

        Keyword argumens:
        forecasts -- the raw parsed data from fetch_forecast().

        Parsing the raw xml-data into a more readable dictionary.

        TODO: Parse directly to this format
        """

        forecast = [
                    {
                'date': f[0],
                'sky': f[1],
                'precipitation': f[2],
                'wind': {
                        'direction': f[3],
                        'speed': f[4]
                },
                'temperature': f[5],
                'pressure': f[6]
                    } for f in forecasts ]
        return forecast

if __name__== "__main__":
    #y = PyYrno("Norway/S%C3%B8r-Tr%C3%B8ndelag/Trondheim/Trondheim", "no")
    b = PyYrno("Norway/Hordaland/Bergen/Bergen/", "en")
    print(b.forecast[0])
