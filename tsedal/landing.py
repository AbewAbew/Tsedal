"""Language-specific landing context, independent of the visitor's LMS language."""
import json
from functools import lru_cache
from pathlib import Path

import frappe
from frappe.utils import get_url


@lru_cache(maxsize=1)
def amharic_copy():
    return json.loads(Path(__file__).with_name("landing_am.json").read_text())


def landing_context(context, language):
    translations = amharic_copy() if language == "am" else {}
    context.language = language
    context.t = lambda text: translations.get(text, text)
    context.english_url = get_url("/en")
    context.amharic_url = get_url("/am")
    context.canonical_url = get_url("/" + language)
    context.no_cache = 1
    return context


def configure_homepage():
    frappe.db.set_single_value("Website Settings", "home_page", "en")
    frappe.clear_cache()
