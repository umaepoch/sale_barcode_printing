frappe.ui.form.on("Sale Barcode Print", {
    sales_order(frm) {
        frappe.call({
            method: "print_labels",
            doc: frm.doc,
            callback: (r) => {
                if (!r.exc) refresh_field("barcode_details");
            },
        });
    }
})
