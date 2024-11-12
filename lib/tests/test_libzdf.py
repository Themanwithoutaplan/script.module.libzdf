import pytest

from ..libzdf import libzdf


@pytest.fixture
def ZDFClient():
    # copied from the configuration of the plugin module
    client = libzdf
    client.baseApi = 'https://api.zdf.de'
    client.userAgent = 'Mozilla/5.0 (X11; Linux x86_64; rv:66.0) Gecko/20100101 Firefox/66.0'
    client.channels =	['ZDF','ZDFinfo','ZDFneo',]
    client.tokenUrl = 'https://zdf-cdn.live.cellular.de/mediathekV2/token'
    client.API_CLIENT_ID = False
    client.API_CLIENT_KEY = False
    client.apiVersion = 2
    return client()


def test_ListMain(ZDFClient):
    client = ZDFClient
    result = client.libZdfListMain()
    assert result == {'items': [{'metadata': {'name': ''},
            'params': {'mode': 'libZdfListPage',
                       'url': 'https://api.zdf.de/content/documents/meist-gesehen-100.json?profile=default'},
            'type': 'dir'},
           {'metadata': {'name': ''},
            'params': {'mode': 'libZdfListShows'},
            'type': 'dir'},
           {'metadata': {'name': ''},
            'params': {'mode': 'libZdfListChannel'},
            'type': 'dir'},
           {'metadata': {'name': ''},
            'params': {'mode': 'libZdfListPage',
                       'url': 'https://api.zdf.de/search/documents?q=%2A&contentTypes=category'},
            'type': 'dir'},
           {'metadata': {'name': ''},
            'params': {'mode': 'libMediathekSearch',
                       'searchMode': 'libZdfListSearch'},
            'type': 'dir'}],
 'name': 'root'}
