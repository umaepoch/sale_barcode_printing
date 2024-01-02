# Copyright (c) 2023, Kanak Infosystems LLP and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from PIL import Image
import requests
from io import BytesIO
import base64
from frappe.core.utils import html2text

class SaleBarcodePrint(Document):
    @frappe.whitelist()
    def get_workorders(self):
        barcode_details = []
        for wo in frappe.get_list("Work Order", fields=["name as name"], filters=[["sales_order", "=", self.sales_order]]):
            work_order = frappe.get_doc("Work Order", wo.get('name'))
            self.append("barcode_details", {
                'product': work_order.item_name,
                'item_code': work_order.production_item,
                'qty': work_order.qty,
                'work_order': work_order.name
            })
        # self.update({'barcode_details':barcode_details})

    @frappe.whitelist()
    def print_labels(self):
        counter = 1
        for line in self.barcode_details:
            product = frappe.get_doc("Item", line.item_code)
            barcode = frappe.generate_hash(line.item_code,10)
            product.update({'barcodes': [{'barcode': barcode}]})
            product.save()
            if product.image:
                file_url = frappe.utils.get_url(product.image)
                r = requests.get(file_url, stream=True)
                url = 'https://www.labelzoom.net/api/v2/convert/png/to/zpl'
                headers = { 'Content-Type': 'image/png', 'Accept': 'text/plain' }
                response = requests.post(url, data=r.content, headers=headers)
                try:
                    zpl = response.text
                    a = zpl.split("^GFA,")
                    b = a[-1].split("^XZ")
                    label = "^XA\n^CF0,50\n^FO30,15^FD%s^FS\n^FO30,60^GB1100,3,3^FS\n^FO30,75^FDMadurai^FS\n^CF0,95\n^FO980,85^FD%s^FS\n^FO30,175^GB1100,3,3^FS\n^CF0,40\n^FO40,190^FDContainer^FS\n^FO30,235^GB1100,3,3^FS\n^FO470,300^GFA,%s\n^CF0,35\n^FO40,575^FD%s^FS\n^FO1050,575^FD%s^FS\n^BY6,2,160\n^FO120,630^BC^FD%s^FS\n^CF0,30\n^FO40,840^FD%s^FS\n^FO1010,840^FD%s^FS\n^FO40,880^GB1100,3,3^FS\n^CF0,130\n^FO40,900^FDSHARK^FS\n^CF0,30\n^FO560,900^FDShark Shopfits Pvt.Ltd^FS\n^FO560,930^FDPlotNo. 29,Udyog Vihar,Echotech II^FS\n^FO560,965^FD201306,Greater Noida (UP)^FS\n^FO560,995^FDPh +91 1204811000^FS\n^XZ" %(barcode,counter,b[0],html2text(product.description),line.package_size,barcode,line.item_code, product.size)
                    line.update({'item_image': label})
                    print(label)
                except requests.exceptions.RequestException:
                    print(response.text)
            else:
                label = "^XA\n^CF0,50\n^FO30,15^FD%s^FS\n^FO30,60^GB1100,3,3^FS\n^FO30,75^FDMadurai^FS\n^CF0,95\n^FO980,85^FD%s^FS\n^FO30,175^GB1100,3,3^FS\n^CF0,40\n^FO40,190^FDContainer^FS\n^FO30,235^GB1100,3,3^FS\n^CF0,35\n^FO40,575^FD%s^FS\n^FO1050,575^FD%s^FS\n^BY6,2,160\n^FO120,630^BC^FD%s^FS\n^CF0,30\n^FO40,840^FD%s^FS\n^FO1010,840^FD%s^FS\n^FO40,880^GB1100,3,3^FS\n^CF0,130\n^FO40,900^FDSHARK^FS\n^CF0,30\n^FO560,900^FDShark Shopfits Pvt.Ltd^FS\n^FO560,930^FDPlotNo. 29,Udyog Vihar,Echotech II^FS\n^FO560,965^FD201306,Greater Noida (UP)^FS\n^FO560,995^FDPh +91 1204811000^FS\n^XZ" %(barcode,counter,b[0],html2text(product.description),line.package_size,barcode,line.item_code, product.size)
                line.update({'item_image': label})
                line.save()
                print(label)
            counter += 1
