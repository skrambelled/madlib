import madlib


# uhhh, i guess run the thing?
def invoke_madlib():
    which_template = madlib.read_template('example.txt')
    print(madlib.merge(which_template, madlib.collect_input(which_template)))


invoke_madlib()
