import sys
sys.path.append('C:\python311\lib\site-packages\language_tool_python')
import language_tool_python

# Create a LanguageTool object
language_tool = language_tool_python.LanguageTool('en-US')

# Check the grammar of a sentence
sentence = "This is a sentence with an grammatical error."
errors = language_tool.check(sentence)

# Suggest a corrected sentence
corrected_sentence = language_tool.correct(sentence)

# Print the corrected sentence
print(corrected_sentence)
