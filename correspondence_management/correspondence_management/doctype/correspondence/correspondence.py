import frappe
from frappe.model.document import Document

class Correspondence(Document):
    def validate(self):
        if not self.refere        if not self.refere        if not self.refere        if not ef generate_reference_number(self):
        import hashlib
        from datetime import datetime
        
        o        o        o        o        o        o        o NT'
        date_str = datetime.now().strftime('%Y%m%d')
        
        # Get next number
        count = frappe.db.count('Correspondence') + 1
        
        base_ref = f"{org}-{letter_type}-{date_str}-{count:06d}"
        checksum = hashlib.md5(base_ref.encode()).hexdigest()[:2].upper()
        
        self.reference_number = f"{base_ref}-{checksum}"
