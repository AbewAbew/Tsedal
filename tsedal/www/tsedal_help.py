import frappe
from tsedal.help_content import GUIDES, SECTIONS

no_cache = 1


def get_context(context):
    slug = frappe.form_dict.get("article") or "introduction"
    if slug not in GUIDES:
        raise frappe.DoesNotExistError
    title, paragraphs = GUIDES[slug]
    context.title = title
    context.paragraphs = paragraphs
    context.slug = slug
    context.sections = [(name, [(key, GUIDES[key][0]) for key in keys]) for name, keys in SECTIONS]
