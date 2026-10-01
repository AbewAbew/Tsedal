app_name = "tsedal"
app_title = "Tsedal"
app_publisher = "Tsedal"
app_description = "Tsedal learning platform customizations"
app_email = "admin@example.com"
app_license = "MIT"
required_apps = ["lms"]
after_install = "tsedal.install.after_install"
after_migrate = "tsedal.branding.apply_branding"

website_route_rules = [
    {"from_route": "/tsedal-help", "to_route": "tsedal_help"},
    {"from_route": "/tsedal-help/<article>", "to_route": "tsedal_help"},
]
