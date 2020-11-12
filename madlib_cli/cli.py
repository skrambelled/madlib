import madlib


# uhhh, i guess run the thing?
def invoke_madlib():
    which_template = madlib.read_template('example.txt')
    merged_madlib = madlib.merge(which_template, madlib.collect_input(which_template))
    print(merged_madlib)
    madlib.write_madlib('example.txt', merged_madlib)


invoke_madlib()
