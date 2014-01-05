#pyyrno

Pyyrno is a simple Python library that gets its data by parsing the forecast XML-feeds provided by yr.no.

## Installation and usage
- Simply place pyyrno.py into your project, and import it. `from pyyrno import PyYrno`.
- Get updated weather data when creating a new instance. `bergen = PyYrno("Norway/Hordaland/Bergen/Bergen/", "no")`, 
builds weather data for the norwegian town Bergen, in norwegian.

Keyword arguments:
-location: format "Country/County/Municipality/City"
-lang: "en": english, "no": norwegian bokmål, "nn": nynorsk

## Data structure
The weather data is accessed with `PyYrno.forecast` built as a dictionary, 
```Python
{
'pressure': {'value': '994.3', 'unit': 'hPa'}, 
'temperature': {'value': '7', 'unit': 'celsius'}, 
'precipitation': {'maxvalue': '2.6', 'minvalue': '0.9', 
'value': '1.7'}, 'date': {'to': '2014-01-05T18:00:00', 
'period': '2', 'from': '2014-01-05T13:00:00'}, 
'sky': {'name': 'Rain', 'number': '9', 'var': '09'}, 
'wind': {
      'direction': {'code': 'SSE', 'name': 'South-southeast', 'deg': '149.3'}, 
      'speed': {'name': 'Fresh breeze', 'mps': '8.0'}
        }
}'
```


Weather forecast from yr.no, delivered by the Norwegian Meteorological Institute and the NRK.
The weather data is provided for free. However, please keep queries down to a minimum, and use cached data when developing. 
