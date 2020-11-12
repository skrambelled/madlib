import re
import os

dirname = os.path.dirname(__file__)


# read a file from the templates/ dir as one string, then return it
def read_template(where):
    if not where:
        return None

    filename = os.path.join(dirname, '../templates')
    template = ''
    with open(f'{filename}/{where}') as in_file:
        for line in in_file:
            template += line

    return template


# return a list only the {enclosed} items in a template
def parse_template(template):
    # lets start with an empty parts list, empty word,
    # and we will not be in capture mode
    parts = []
    word = ''
    capture = False

    # now loop through each char in the template
    for char in template:
        if capture:
            # turn off capturee mode, and send the captured
            # word to the parts list
            if char == '}':
                capture = False
                parts += [word]
            # capture another character into our word
            else:
                word += char
        else:
            # turn on capture mode, and reset word when we hit an opening `{`
            if char == '{':
                capture = True
                word = ''
    return parts


# remove the internal portions of {} in a string and return the result
def remove_template_words(template):
    return re.sub("{.*?}", "{}", template)


# prompt the user for a number of madlibs, based on a template
def collect_input(template):
    user_words = []
    template_words = parse_template(template)

    for word in template_words:
        user_words += [input(f"Input a '{word}'> ")]

    return user_words


# merge a list of supplied madlibs with a template
def merge(template, user_words):
    template = remove_template_words(template)
    for word in user_words:
        template = template.replace('{}', word, 1)
    return template
