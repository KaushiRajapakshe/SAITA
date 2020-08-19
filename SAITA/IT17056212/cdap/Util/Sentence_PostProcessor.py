import language_check


def sentence_validate(text):
    tool = language_check.LanguageTool('en-US')

    matches = tool.check(text)
    print(len(matches))
    corrected = language_check.correct(text, matches)

    if len(matches) == 1 or len(matches) == 0:
        return "correct"
    else:
        print("Corrected: " + corrected)
        return "incorrect"
