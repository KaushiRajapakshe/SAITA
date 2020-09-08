def get_phrases():
    keep_phrases = ["Address already in use", "Unable to open logs", "ReservedCodeCacheSize=240m",
                    "Application run failed", "objectMapperConfigurer"]
    return keep_phrases


# time regular expression pattern 01 for 2020 21:02:03
def get_regular_expression1():
    regular_expression = r"[0-9][0-9].[0-9][0-9]\:[0-9][0-9]\:[0-9][0-9]"
    return regular_expression
