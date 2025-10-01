import frappe
from frappe import _
import hashlib
from datetime import datetime

@frappe.whitelist()
def generate_reference(doc, method=None):
    """Generate unique reference number"""
    if isinstance(doc, str):
        doc = frappe.get_doc('Correspondence', doc)
    
    if doc.reference_number:
        return
    
    org = frappe.db.get_single_value('Global Defaults', 'default_company_abbr') or 'ORG'
    letter_type = doc.letter_type or 'INT'
    date_str = datetime.now().strftime('%Y%m%d')
    
    dept_code = 'GEN'
    if doc.department:
        dept_code = frappe.db.get_value('Department', doc.department, 'abbr') or 'GEN'
    
    # Get next number
    last_num = frappe.db.sql("""
        SELECT MAX(CAST(SUBSTRING_INDEX(SUBSTRING_INDEX(reference_number, '-', 5), '-', -1) AS UNSIGNED))
        FROM `tabCorrespondence`
        WHERE reference_number LIKE %s
    """, f"{org}-{letter_type}-{date_str}-%")
    
    next_num = (last_num[0][0] or 0) + 1 if la    next_num = (last_num[0][0] or 0) + 1 ibase_ref = f"{org}-{letter_type}-{date_str}-{dept_code}-{next_num:06d}"
    checksum = hashlib.md5(base_ref.encode()).hexdigest()[:2].upper()
    
    doc.reference_number = f"{base_ref}-{checksum}"

@frappe.whitelist()
defdefdefdefdefdefdefdefdefdefdefdefdefdefdefdefdefde to department secretary"""
    if isinstance(doc, str):    if isinstance(doc, str):    if isinstance(doc, str):    if isinstance(doc, str):  t doc.assigned_to:
        secretary = frappe.db.get_value('Department', doc.department, 'custom_secretary')
        if secretary:
            do            do            do            do            do            do            dodoc, method=None):
    """Check SLA status"""
    if isinstance(doc, str):
        doc = frappe.get_doc('Correspondence', doc)
    
    if doc.response_due_date and doc.workflow_state != 'Completed':
        from frappe.utils import now_datetime
        if now_datetime() > doc.response_due_date:
            frappe.publish_realtime('sla_breach', {
                'document': doc.name,
                'reference': doc.reference_number
            })
