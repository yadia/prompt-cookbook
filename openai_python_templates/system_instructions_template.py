# Tempalte for system instructions

#text for user input
text = "Say hello world"

# System instructions with limitations.
system_instruction = f""" Perform the following actions :  1. \
3. If the text provided does not contain
4. If you do not know the answer reply \"I can not provide an answer for this. Ask another question. \"
Separate your answer with line breaks.\
''' {text} ''' 
"""