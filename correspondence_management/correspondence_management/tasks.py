import frappe
from frappe.utils import nowdate, add_days

def check_overdue():
    """Check for overdue correspondence"""
    overdue = frappe.db.sql("""
        SELECT name, reference_number, assigned_to
        FROM `tabCorrespondence`
        WHERE response_due_date < %s
        AND workflow_state NOT IN ('Completed', 'Cancelled')
    """, nowdate(), as_dict=1)
    
    for doc in overdue:
        # Send notification
        if doc.assigned_to:
            frappe.sendmail(
                recipients=[doc.assigned_to],
                subject=f"Overdue: {doc.reference_number}",
                message="This correspondence is overdue. Please take action."
            )

def process_ocr_queue():
    """Process pending OCR jobs"""
    pending = frappe.db.sql("""
        SELECT name 
        FROM `tabCorrespondence`
        WHERE scan_file IS NOT NULL
        AND ocr_status = 'Pending'
        LIMIT 5
    """, as_dict=1)
    
    for doc in pending:
        process_ocr(doc.name)

def process_ocr(doc_name):
    """Process OCR for a document"""
    doc = frappe.get_doc('Correspondence', doc_name)
    doc.ocr_status = 'Processing'
                                ur OCR processing logic here
    # For Frappe Cloud, use external API
    
    doc.ocr    doc.ocr    doc.ocr    doc.ocr  )
