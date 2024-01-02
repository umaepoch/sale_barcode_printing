from . import __version__ as app_version

app_name = "sale_barcode_printing"
app_title = "Sale Barcode Printing"
app_publisher = "Kanak Infosystems LLP"
app_description = "This app will give a feature to print sale barcode."
app_email = "sales@kanakinfosystems.com"
app_license = "AGPL"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/sale_barcode_printing/css/sale_barcode_printing.css"
# app_include_js = "/assets/sale_barcode_printing/js/sale_barcode_printing.js"

# include js, css files in header of web template
# web_include_css = "/assets/sale_barcode_printing/css/sale_barcode_printing.css"
# web_include_js = "/assets/sale_barcode_printing/js/sale_barcode_printing.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "sale_barcode_printing/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"Sale Barcode Print" : "public/js/sale_barcode_print.js"}
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

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
#	"methods": "sale_barcode_printing.utils.jinja_methods",
#	"filters": "sale_barcode_printing.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "sale_barcode_printing.install.before_install"
# after_install = "sale_barcode_printing.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "sale_barcode_printing.uninstall.before_uninstall"
# after_uninstall = "sale_barcode_printing.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "sale_barcode_printing.utils.before_app_install"
# after_app_install = "sale_barcode_printing.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "sale_barcode_printing.utils.before_app_uninstall"
# after_app_uninstall = "sale_barcode_printing.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "sale_barcode_printing.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
#	"*": {
#		"on_update": "method",
#		"on_cancel": "method",
#		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"sale_barcode_printing.tasks.all"
#	],
#	"daily": [
#		"sale_barcode_printing.tasks.daily"
#	],
#	"hourly": [
#		"sale_barcode_printing.tasks.hourly"
#	],
#	"weekly": [
#		"sale_barcode_printing.tasks.weekly"
#	],
#	"monthly": [
#		"sale_barcode_printing.tasks.monthly"
#	],
# }

# Testing
# -------

# before_tests = "sale_barcode_printing.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "sale_barcode_printing.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "sale_barcode_printing.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["sale_barcode_printing.utils.before_request"]
# after_request = ["sale_barcode_printing.utils.after_request"]

# Job Events
# ----------
# before_job = ["sale_barcode_printing.utils.before_job"]
# after_job = ["sale_barcode_printing.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
#	{
#		"doctype": "{doctype_1}",
#		"filter_by": "{filter_by}",
#		"redact_fields": ["{field_1}", "{field_2}"],
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_2}",
#		"filter_by": "{filter_by}",
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_3}",
#		"strict": False,
#	},
#	{
#		"doctype": "{doctype_4}"
#	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"sale_barcode_printing.auth.validate"
# ]
