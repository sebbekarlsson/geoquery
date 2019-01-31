# geoquery
> Find the name of a location by using latitude and longitude.

## Usage
> To use:

    from geoquery import query

    
    for location in query(
        'SE',
        dict(
            latitude=57.7166777,
            longitude=11.7579122)
        )
    ):
        print(location)

> The query method will return a list of dictionaries, looking like this:

    {
        "admin1_code": "28", 
        "admin2_code": "1480", 
        "admin3_code": "", 
        "admin4_code": "", 
        "alternate": "", 
        "asciiname": "Bur", 
        "cc2": "", 
        "country_code": "SE", 
        "dem": "29", 
        "elevation": "", 
        "feature_class": "P", 
        "feature_code": "PPL", 
        "geonameid": "3331634", 
        "latitude": 57.71667, 
        "longitude": 11.78333, 
        "modification_date": "2011-10-30", 
        "name": "Bur", 
        "population": "0", 
        "score": 98.0, 
        "timezone": "Europe/Stockholm"
    }
    {
        "admin1_code": "28", 
        "admin2_code": "", 
        "admin3_code": "", 
        "admin4_code": "", 
        "alternate": "", 
        "asciiname": "Sodra Hasteviken", 
        "cc2": "", 
        "country_code": "SE", 
        "dem": "9", 
        "elevation": "", 
        "feature_class": "H", 
        "feature_code": "COVE", 
        "geonameid": "3331635", 
        "latitude": 57.71667, 
        "longitude": 11.71667, 
        "modification_date": "2001-06-28", 
        "name": "S\u00f6dra H\u00e4steviken", 
        "population": "0", 
        "score": 98.0, 
        "timezone": "Europe/Stockholm"
    }

# To install
> Using pip:

    pip install geoquery

> Using git, clone down repo and run:

    python setup.py install
