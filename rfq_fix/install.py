import os
import frappe
import shutil


def replace_rfq_js():
    """replace the default rfq in the js
        to fix the issue with parsefloat 
        ex parsefloat("1,000.00") returns 1 instead of 1000
    """
    try:
        
        destination_path  = frappe.utils.get_bench_path() + "/apps/erpnext/erpnext/templates/includes/rfq.js"
        source = frappe.utils.get_bench_path() + "/apps/rfq_fix/rfq_fix/rfq.js"
        if os.path.exists(source):
            os.replace(source, destination_path)
    except Exception as e:
        print(e)
        