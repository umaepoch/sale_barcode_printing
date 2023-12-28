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
    def print_labels(self):
        # sale = frappe.get_doc("Sales Order", self.sales_order)
        # company = frappe.get_doc("Company", sale.company)
        # file_url = frappe.utils.get_url(company.company_logo)
        # r = requests.get(file_url, stream=True)
        # url = 'https://www.labelzoom.net/api/v2/convert/png/to/zpl'
        # headers = { 'Content-Type': 'image/png', 'Accept': 'text/plain' }
        # response = requests.post(url, data=r.content, headers=headers)
        # company_logo = False
        # try:
        #     zpl = response.text
        #     a = zpl.split("^GFA,")
        #     b = a[-1].split("^XZ")
        #     company_logo = b[0]
        # except requests.exceptions.RequestException:
        #     print(response.text)
        barcode_details = []
        for wo in frappe.get_list("Work Order", fields=["name as name"], filters=[["sales_order", "=", self.sales_order]]):
            work_order = frappe.get_doc("Work Order", wo.get('name'))
            barcode_details.append({
                'product': work_order.item_name,
                'item_code': work_order.production_item,
                'qty': work_order.qty,
                'work_order': work_order.name

            })
        self.update({'barcode_details':barcode_details})
        counter = 1
        for line in self.barcode_details:
            product = frappe.get_doc("Item", line.item_code)
            barcode = frappe.generate_hash(line.item_code,10)
            file_url = frappe.utils.get_url(product.image)
            r = requests.get(file_url, stream=True)
            url = 'https://www.labelzoom.net/api/v2/convert/png/to/zpl'
            headers = { 'Content-Type': 'image/png', 'Accept': 'text/plain' }
            response = requests.post(url, data=r.content, headers=headers)
            try:
                zpl = response.text
                a = zpl.split("^GFA,")
                b = a[-1].split("^XZ")
                label = "^XA\n^CF0,20\n^FO20,10^FD%s^FS\n^FO20,30^GB750,3,3^FS\n^FO20,40^FDMadurai^FS\n^FO700,40^FD%s^FS\n^FO20,70^GB750,3,3^FS\n^CF0,30\n^FO20,80^FDContainer^FS\n^FO20,110^GB750,3,3^FS\n^FO100,120^GFA,%s\n^CF0,20\n^FO20,430^FD%s^FS\n^FO700,430^FD%s^FS\n^BY3,2,150\n^FO20,450^BC^FD%s^FS\n^FO20,660^FD%s^FS\n^FO600,660^FD%s^FS\n^FO20,680^GB750,3,3^FS\n^CF0,110\n^FO20,700^FDSHARK^FS\n^CF0,20\n^FO500,700^FDShark Shopfits Pvt.Ltd^FS\n^FO500,720^FDPlotNo. 29,Udyog Vihar,Echotech II^FS\n^FO500,740^FD201306,Greater Noida (UP)^FS\n^FO500,760^FDPh +91 1204811000^FS\n^XZ" %(barcode,counter,b[0],html2text(product.description),line.package_size,barcode,line.item_code, product.size)
                line.update({'item_image': label})
                print(label)
            except requests.exceptions.RequestException:
                print(response.text)
            counter += 1

    # @frappe.whitelist()
    # def print_labels(self):
    #     url = 'https://drive.google.com/uc?export=download&id=17-p_7-CzC5DHqi2Nv9Jmd7rZyGVjVveF'
    #     file_url = frappe.utils.get_url(url)
    #     r = requests.get(file_url, stream=True)
    #     url = 'https://www.labelzoom.net/api/v2/convert/png/to/zpl'
    #     headers = { 'Content-Type': 'image/png', 'Accept': 'text/plain' }
    #     response = requests.post(url, data=r.content, headers=headers)
    #     try:
    #         zpl = response.text
    #         print(zpl)
    #     except requests.exceptions.RequestException:
    #         print(response.text)