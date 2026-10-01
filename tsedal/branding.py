"""Idempotent Tsedal branding for website pages and the administrator Desk."""
import frappe


def apply_branding():
    website = frappe.get_single("Website Settings")
    website.app_name = "Tsedal"
    # A non-empty override suppresses the framework's default footer attribution.
    website.footer_powered = "<!-- Tsedal -->"
    website.save(ignore_permissions=True)

    navbar = frappe.get_single("Navbar Settings")
    for item in navbar.help_dropdown:
        # Preserve standard rows and useful keyboard shortcuts; hide upstream
        # support/about destinations without modifying their implementation.
        target = " ".join(str(item.get(key) or "") for key in ("item_label", "route", "action"))
        if "show_about" in target or "frappe.io" in target or "Frappe" in target:
            item.hidden = 1

    for label, route in [
        ("Tsedal Help", "/tsedal-help"),
        ("Tsedal Administrator Guide", "/tsedal-help/administrator"),
        ("Tsedal Student Guide", "/tsedal-help/student"),
        ("About Tsedal", "/tsedal-help/about"),
    ]:
        if not any(item.route == route for item in navbar.help_dropdown):
            navbar.append("help_dropdown", {"item_label": label, "item_type": "Route", "route": route})
    navbar.save(ignore_permissions=True)
    frappe.clear_cache()
