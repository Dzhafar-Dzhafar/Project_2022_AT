from my_funcs.file_work import read_from_file

def test_read_from_file():
    test_data = 'one\ntwo\nthree'
    assert test_data == read_from_file("test_file.txt")
