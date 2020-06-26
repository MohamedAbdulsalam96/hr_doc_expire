from __future__ import unicode_literals
import frappe
from frappe.utils import date_diff, nowdate, add_days, format_datetime
from datetime import timedelta, datetime


def expire_doc_mail_notify():
    # stuff to do every 10 minutes
    today = nowdate()
    employee_documents = frappe.db.get_list('Employee Documents',
                                            fields=['parent', 'doc_name', 'reminder_days', 'expire_date'],
                                            filters={"expire_date": (">", today)})
    for record in employee_documents:
        expire_date = record.get('expire_date') - timedelta(days=record.get('reminder_days'))
        if expire_date == datetime.today().date():
            employee_id = frappe.get_doc("Employee", {"name": record.get('parent')}).as_dict()
            recipients = []
            if employee_id.prefered_email:
                recipients.append(employee_id.prefered_email)
            if employee_id.company_email:
                recipients.append(employee_id.company_email)
            if employee_id.personal_email:
                recipients.append(employee_id.personal_email)
            for company in frappe.db.get_all("Company"):
                company = frappe.get_doc("Company", company.name)
                recipients.append(company.email)
            if recipients:
                frappe.sendmail(recipients=recipients, subject=frappe._('Document Will Expire Soon!'),
                                message='Your document {0} will expire soon\n Please Renew asap \n Kind Regards'.format(
                                    record.get('doc_name')))
