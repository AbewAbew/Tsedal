from tsedal.landing import landing_context

no_cache = 1


def get_context(context):
    return landing_context(context, "en")
