import language_tool_python

def grammar_check(sentence):
    # Initialize the LanguageTool tool
    tool = language_tool_python.LanguageTool('en-US')

    # Check the sentence for errors
    matches = tool.check(sentence)

    # If there are no errors, return the original sentence
    if not matches:
        return sentence

    # Correct the errors in the sentence
    corrected_sentence = tool.correct(sentence)
    return corrected_sentence