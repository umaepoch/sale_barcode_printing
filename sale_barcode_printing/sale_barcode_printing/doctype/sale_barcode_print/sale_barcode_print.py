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
    # @frappe.whitelist()
    # def get_workorders(self):
    #     barcode_details = []
    #     workk_orders = []
    #     for wo in frappe.get_list("Work Order", fields=["name as name"], filters=[["sales_order", "=", self.sales_order]]):
    #         work_order = frappe.get_doc("Work Order", wo.get('name'))
    #         if work_order.name not in workk_orders:
    #             product = frappe.get_doc("Item", work_order.item_name)
    #             barcode_details.append({
    #                 'product': work_order.item_name,
    #                 'item_code': work_order.production_item,
    #                 'qty': work_order.qty,
    #                 'work_order': work_order.name,
    #                 'package_size': product.package_size
    #             })
    #             workk_orders.append(work_order.name)
    #     self.update({'barcode_details':barcode_details})

    @frappe.whitelist()
    def print_labels(self):
        barcode_details = []
        workk_orders = []
        so = self.sales_order
        store_location = frappe.db.get_value('Sales Order', so, 'store_location')
        project_format = frappe.db.get_value('Sales Order', so, 'project_format')
        for wo in frappe.get_list("Work Order", fields=["name as name"], filters=[["sales_order", "=", self.sales_order],['status', '=', 'Completed']]):
            work_order = frappe.get_doc("Work Order", wo.get('name'))
            if work_order.name not in workk_orders:
                product = frappe.get_doc("Item", work_order.production_item)
                barcode_details.append({
                    'product': work_order.item_name,
                    'item_code': work_order.production_item,
                    'qty': work_order.qty,
                    'work_order': work_order.name,
                    'package_size': product.package_size
                })
                workk_orders.append(work_order.name)
        self.update({'barcode_details':barcode_details})
        counter = 1
        for line in self.barcode_details:
            product = frappe.get_doc("Item", line.item_code)
            if not product.barcodes:
                barcode = frappe.generate_hash(line.item_code,10)
                product.update({'barcodes': [{'barcode': barcode}]})
                product.save()
            else:
                barcode = product.barcodes[0].barcode
            product_desc = ''
            if product.description:
                product_desc = html2text(product.description)
                if len(product.description) > 40:
                    product_desc = product_desc[:40]
                else:
                    product_desc = product_desc
            if product.image:
                file_url = frappe.utils.get_url(product.image)
                r = requests.get(file_url, stream=True)
                url = 'https://www.labelzoom.net/api/v2/convert/png/to/zpl'
                headers = { 'Content-Type': 'image/png', 'Accept': 'text/plain' }
                response = requests.post(url, data=r.content, headers=headers)
                try:
                    zpl = response.text
                    a = zpl.split("^GFA,")
                    if a:
                        b = a[-1].split("^XZ")
                        label = "^XA\n^CF0,50\n^FO30,35^FD%s^FS\n^FO30,90^GB1100,3,3^FS\n^FO30,105^FD%s^FS\n^CF0,50\n^FO820,125^FD%s^FS\n^FO30,235^GB1100,3,3^FS\n^CF0,40\n^FO40,250^FDContainer^FS\n^FO30,295^GB1100,3,3^FS\n^FO470,340^GFA,%s\n^CF0,35\n^FO40,625^FD%s^FS\n^FO1050,575^FD%s^FS\n^BY6,2,160\n^FO120,690^BC^FD%s^FS\n^CF0,30\n^FO40,920^FD%s^FS\n^FO970,910^FD%s^FS\n^FO40,960^GB1100,3,3^FS\n^CF0,150\n^FO40,1010^FDSHARK^FS\n^CF0,30\n^FO590,1000^FDShark Shopfits Pvt.Ltd^FS\n^FO590,1040^FDPlotNo. 29,Udyog Vihar,Echotech II^FS\n^FO590,1085^FD201306,Greater Noida (UP)^FS\n^FO590,1130^FDPh +91 1204811000^FS\n^XZ" %(project_format,counter,store_location,b[0],product_desc,line.package_size,barcode,line.item_code, product.size)
                        line.update({'item_image': label})
                        print(label)
                    else:
                        label = "^XA\n^CF0,50\n^FO30,35^FD%s^FS\n^FO30,90^GB1100,3,3^FS\n^FO30,105^FD%s^FS\n^CF0,50\n^FO820,125^FD%s^FS\n^FO30,235^GB1100,3,3^FS\n^CF0,40\n^FO40,250^FDContainer^FS\n^FO30,295^GB1100,3,3^FS\n^CF0,35\n^FO40,625^FD%s^FS\n^FO1050,575^FD%s^FS\n^BY6,2,160\n^FO120,690^BC^FD%s^FS\n^CF0,30\n^FO40,920^FD%s^FS\n^FO970,910^FD%s^FS\n^FO40,960^GB1100,3,3^FS\n^CF0,150\n^FO40,1010^FDSHARK^FS\n^CF0,30\n^FO590,1000^FDShark Shopfits Pvt.Ltd^FS\n^FO590,1040^FDPlotNo. 29,Udyog Vihar,Echotech II^FS\n^FO590,1085^FD201306,Greater Noida (UP)^FS\n^FO590,1130^FDPh +91 1204811000^FS\n^XZ" %(project_format,counter,store_location,product_desc,line.package_size,barcode,line.item_code, product.size)
                        line.update({'item_image': label})
                        line.save()
                except requests.exceptions.RequestException:
                    print(response.text)
            else:
                label = "^XA\n^CF0,50\n^FO30,35^FD%s^FS\n^FO30,90^GB1100,3,3^FS\n^FO30,105^FD%s^FS\n^CF0,50\n^FO820,125^FD%s^FS\n^FO30,235^GB1100,3,3^FS\n^CF0,40\n^FO40,250^FDContainer^FS\n^FO30,295^GB1100,3,3^FS\n^CF0,35\n^FO40,625^FD%s^FS\n^FO1050,575^FD%s^FS\n^BY6,2,160\n^FO120,690^BC^FD%s^FS\n^CF0,30\n^FO40,920^FD%s^FS\n^FO970,910^FD%s^FS\n^FO40,960^GB1100,3,3^FS\n^CF0,150\n^FO40,1010^FDSHARK^FS\n^CF0,30\n^FO590,1000^FDShark Shopfits Pvt.Ltd^FS\n^FO590,1040^FDPlotNo. 29,Udyog Vihar,Echotech II^FS\n^FO590,1085^FD201306,Greater Noida (UP)^FS\n^FO590,1130^FDPh +91 1204811000^FS\n^XZ" %(project_format,counter,store_location,product_desc,line.package_size,barcode,line.item_code, product.size)
                line.update({'item_image': label})
                line.save()
                print(label)
            counter += 1
        self.save()
