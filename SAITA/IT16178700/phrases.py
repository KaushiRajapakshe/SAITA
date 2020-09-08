def get_phrases():
    keep_phrases = ["Address already in use", "Unable to open logs", "ReservedCodeCacheSize=240m",
                    "Application run failed", "objectMapperConfigurer"]
    return keep_phrases


# time regular expression pattern 01 for 2020 21:02:03
def get_regular_expression1():
    regular_expression = r"[0-9][0-9].[0-9][0-9]\:[0-9][0-9]\:[0-9][0-9]"
    return regular_expression


# time regular expression pattern 02 for 2020 9:02:03 PM
def get_regular_expression2():
    regular_expression = r"[0-9][0-9].[0-9]\:[0-9][0-9]\:[0-9][0-9]"
    return regular_expression
