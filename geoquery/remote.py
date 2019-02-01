from StringIO import StringIO
from zipfile import ZipFile
from urllib import urlopen
import os


def download_and_read(country_code, use_cache=True):
    fname = country_code.upper() + '.txt'
    cachepath = '/tmp/' + fname

    if use_cache and os.path.isfile(cachepath):
        return open(cachepath).readlines()

    lines = ZipFile(StringIO(urlopen(
        'http://download.geonames.org/export/dump/{}.zip'
        .format(country_code.upper())
    ).read())).open(fname).readlines()

    open(cachepath, 'w+').writelines(lines)

    return lines
