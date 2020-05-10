
def get_phrases():
    keep_phrases = ["Address already in use", "Unable to open logs", "ReservedCodeCacheSize=240m",
                    "Application run failed", "objectMapperConfigurer"]
    return keep_phrases


# time regular expression pattern
def get_regular_expression():
    regular_expression = r"[0-9][0-9].[0-9][0-9]\:[0-9][0-9]\:[0-9][0-9]"
    return regular_expression
