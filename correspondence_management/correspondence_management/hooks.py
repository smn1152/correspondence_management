from . import __version__ as app_version

app_name = "correspondence_management"
app_title = "Correspondence Management"
app_publisher = "Your Company"
app_description = "Enterprise Correspondence Management System"
app_email = "admin@company.com"
app_license = "MIT"

required_apps = ["frappe", "erpnext"]

fixtures = [
    {
        "dt": "Workflow",
        "filters": {"name": ["in", ["Correspondence Workflow"]]}
    },
    {
        "dt": "Role",
        "filters": {"name": ["in", ["Correspondence Clerk", "Department Secretary", "Correspondence Manager"]]}
    }
]

doc_events = {
    "Correspondence": {
        "before_insert": "correspondence_management.utils.generate_reference",
        "after_insert": "correspondence_management.utils.auto_assign",
        "on_update": "correspondence_management.utils.check_sla"
    }
}

scheduler_events = {
    "daily": [
        "correspondence_management.tasks.check_overdue"
    ],
    "hourly": [
        "correspondence_management.tasks.process_ocr_queue"
    ]
}
