from madlib_cli.madlib import read_template, parse_template, remove_template_words, collect_input, merge


def test_imports():
    assert read_template
    assert parse_template
    assert remove_template_words
    assert collect_input
    assert merge


def test_read_template():
    actual = read_template('test.txt')
    expect = "This is a {test}"
    assert actual == expect


def test_parse_template():
    actual = parse_template(read_template('test.txt'))
    expect = ['test']
    assert actual == expect


def test_remove_template_words():
    actual = remove_template_words('these {are} some {words}')
    expect = 'these {} some {}'
    assert actual == expect


def test_merge():
    print(remove_template_words('some {words} to {test}'))
    actual = merge('some {words} to {test}', ['one', 'two'])
    expect = 'some one to two'
    assert actual == expect
