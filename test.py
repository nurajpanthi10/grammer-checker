# import language_tool_python

# # Initialize LanguageTool
# tool = language_tool_python.LanguageTool('en-US')

# def get_correction(sentence):
#     # Check the sentence for grammar and style errors
#     matches = tool.check(sentence)

#     # If there are no errors, return the original sentence
#     if not matches:
#         return sentence

#     # If there are errors, apply corrections
#     corrected_sentence = tool.correct(sentence)
#     return corrected_sentence

# # User input
# user_input = input("Enter a sentence: ")

# # Get and display the corrected sentence
# corrected_output = get_correction(user_input)
# print(f"Corrected Sentence: {corrected_output}")
# import spacy

# import Caribe as cb
# sentence="I is playing football"
# output=cb.caribe_corrector(sentence)
# print(output)


import language_tool_python

def correct_sentence(sentence):
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

