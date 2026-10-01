"""Local development server bound only to loopback."""
import os
from pathlib import Path

os.chdir(Path(__file__).resolve().parent.parent / "bench/sites")

import frappe.app
from werkzeug.serving import run_simple

frappe.app._sites_path = "."
run_simple("127.0.0.1", 18780, frappe.app.application_with_statics(),
           use_reloader=False, use_debugger=False, threaded=True)
