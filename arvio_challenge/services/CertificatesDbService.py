from ..helpers import utils
from django.shortcuts import get_object_or_404
from django.http import HttpResponseNotAllowed
from ..models import EnergyCertificate

def getCertificateById(property_id):
    if utils.validate_property(property_id):
        obj = get_object_or_404(EnergyCertificate, property_id=property_id)
        return obj
    else:
        raise ValueError("Property id is malformed")

