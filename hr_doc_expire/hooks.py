# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "hr_doc_expire"
app_title = "Employee Document Expire"
app_publisher = "Mostafa Mohamed"
app_description = "Manage employee documents within the company"
app_icon = "fa fa-book"
app_color = "grey"
app_email = "m.dev.odoo@gmail.com"
app_license = "MIT"
fixtures = [{"dt":"Custom Field", "filters": [["dt", "in", ("Employee")]]}]
# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/hr_doc_expire/css/hr_doc_expire.css"
# app_include_js = "/assets/hr_doc_expire/js/hr_doc_expire.js"

# include js, css files in header of web template
# web_include_css = "/assets/hr_doc_expire/css/hr_doc_expire.css"
# web_include_js = "/assets/hr_doc_expire/js/hr_doc_expire.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "hr_doc_expire.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "hr_doc_expire.install.before_install"
# after_install = "hr_doc_expire.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "hr_doc_expire.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
	"Employee": {
		"validate": "hr_doc_expire.custom_methods.hr_custom.employee_doc_count",
	}
}

# Scheduled Tasks
# ---------------
scheduler_events = {
    "cron": {
        "00 9 * * *": [
            "hr_doc_expire.tasks.expire_doc_mail_notify"
        ]
    }
}

# Testing
# -------

# before_tests = "hr_doc_expire.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "hr_doc_expire.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "hr_doc_expire.task.get_dashboard_data"
# }

