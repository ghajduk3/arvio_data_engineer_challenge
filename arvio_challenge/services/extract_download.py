from . import downloader,extractor
from .. import models
from ..helpers import utils,bulk_create_manager
import os

def extract_and_download(url_list_path=None):
    if not url_list_path:
        url_list_path = os.path.join(os.path.abspath(os.path.dirname(__name__)),'data/url_list.csv')
    download = downloader.Downloader()
    extract = extractor.Extractor()
    bulk_mgr = bulk_create_manager.BulkCreateManager(chunk_size=20)
    url_list = utils.read_url_list(url_list_path)
    models.EnergyCertificate.objects.all().delete()
    for url in url_list:
        cert_id,municipality,building,units,heat_lvl = extract.extract_data(download.download(url,'https://whats-that.s3.eu-central-1.amazonaws.com/energy-data/'))
        for unit in units:
            property_id = municipality + '-' + building + '-' + str(unit)
            bulk_mgr.add(models.EnergyCertificate(property_id=property_id,certificate_id=cert_id,municipality=int(municipality),building=int(building),unit=unit,heat_efficiency_lvl=heat_lvl))



