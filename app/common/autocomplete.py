from english_words import english_words_lower_alpha_set
# import re

class Autocomplete:
    # wordlist = ['one','two','three','only']

    def match(partial):
        # matches = [word for word in Autocomplete.wordlist if re.search(partial, word)]
        # matches = [word for word in Autocomplete.wordlist if partial in word]

        # words = [word for word in Autocomplete.wordlist if partial in word]
        # matches = []
        # if len(words) > 0:
        #     matches = [word for word in words if word.index(partial) == 0]

        # matches = [word for word in Autocomplete.wordlist if word.startswith(partial)]
        matches = [word for word in english_words_lower_alpha_set if word.startswith(partial)]
        return matches
