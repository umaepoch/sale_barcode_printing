# Copyright (c) 2023, Kanak Infosystems LLP and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from PIL import Image
import requests
from io import BytesIO
import base64

class SaleBarcodePrint(Document):
    @frappe.whitelist()
    def print_labels(self):
        url = 'https://drive.google.com/uc?export=download&id=17-p_7-CzC5DHqi2Nv9Jmd7rZyGVjVveF'
        file_url = frappe.utils.get_url(url)
        r = requests.get(file_url, stream=True)
        url = 'https://www.labelzoom.net/api/v2/convert/png/to/zpl'
        headers = { 'Content-Type': 'image/png', 'Accept': 'text/plain' }
        response = requests.post(url, data=r.content, headers=headers)
        try:
            zpl = response.text
            print(zpl)
        except requests.exceptions.RequestException:
            print(response.text)