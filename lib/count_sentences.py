# #!/usr/bin/env python3
import re

class MyString:
    def __init__(self, value=''):
        self.value = value

    def __setattr__(self, name, value):
        '''Override to ensure value is a string and handle printing error message.'''
        if name == 'value':
            if not isinstance(value, str):
                print("The value must be a string.")
            else:
                super().__setattr__(name, value)
        else:
            super().__setattr__(name, value)

    def is_sentence(self):
        '''Returns True if the string ends with a period, False otherwise.'''
        return self.value.endswith('.')

    def is_question(self):
        '''Returns True if the string ends with a question mark, False otherwise.'''
        return self.value.endswith('?')

    def is_exclamation(self):
        '''Returns True if the string ends with an exclamation mark, False otherwise.'''
        return self.value.endswith('!')

    def count_sentences(self):
        '''Returns the number of sentences in the string.'''
        # Regular expression to split on sentence-ending punctuation (., !, ?)
        sentences = re.split(r'[.!?]+', self.value)
        
        # Filter out empty strings
        return len([sentence for sentence in sentences if sentence.strip()])
