import frappe


def after_install():
    website = frappe.get_single("Website Settings")
    website.app_name = "Tsedal"
    website.brand_html = "Tsedal"
    website.home_page = "lms"
    website.save(ignore_permissions=True)
    settings = frappe.get_single("System Settings")
    settings.language = settings.language or "en"
    settings.time_zone = "Africa/Addis_Ababa"
    settings.save(ignore_permissions=True)
