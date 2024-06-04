class MyString:
    def __init__(self, value=''):
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if isinstance(value, str):
            self._value = value
        else:
            raise ValueError("Value must be a string")

    def is_sentence(self):
        return self.value.endswith('.')

    def is_question(self):
        return self.value.endswith('?')

    def is_exclamation(self):
        return self.value.endswith('!')

    def count_sentences(self):
       
        import re
        cleaned_value = re.sub(r'[.!?]+', '.', self.value)
        
        sentences = [s.strip() for s in cleaned_value.split('.') if s.strip()]
        return len(sentences)
