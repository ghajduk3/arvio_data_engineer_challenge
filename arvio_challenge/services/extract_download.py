from . import downloader,extractor
from .. import models
from ..helpers import utils,BulkCreateManager
import os

def extract_and_download(url_list_path=None):
    if not url_list_path:
        url_list_path = os.path.join(os.path.abspath(os.path.dirname(__name__)),'data/url_list.csv')
    download = downloader.Downloader()
    extract = extractor.Extractor()
    bulk_mgr = BulkCreateManager.BulkCreateManager(chunk_size=20)
    url_list = utils.read_url_list(url_list_path)
    print(url_list)
    # First drops all
    # models.EnergyCertificate.objects.all().delete()
    for url in url_list:
        print(url)
        cert_id,municipality,building,units,heat_lvl = extract.extract_data(download.download(url,'https://whats-that.s3.eu-central-1.amazonaws.com/energy-data/'))
        print(cert_id)
        for unit in units:
            property_id = municipality + '-' + building + '-' + str(unit)
            bulk_mgr.add(models.EnergyCertificate(property_id=property_id,certificate_id=cert_id,municipality=int(municipality),building=int(building),unit=unit,heat_efficiency_lvl=heat_lvl))



