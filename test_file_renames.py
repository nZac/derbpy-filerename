'''
Given a filename of format with the following sections separated by a space,

1. A two digit number : ID
2. A dash : ID Separator
3. The word Tape followed by a number : Tape number
4. The word Side followed by a number : Side ID
5. A dash : Title Separator
6. A Title (which could have a space) ***** : Title
7. A single or two digit number
8. The file type

'30 - Tape30 Side2 - L. Ron Hubbard 1.mp3'

Write a function which returns a dictionary of the individual parts except the separators.
'''
from file_renamer import title_parser, filenamer

def test_title_parser_returns_a_dictionary():
    assert isinstance(title_parser(''), dict)

def test_title_parser_returns_a_six_item_dictionary():
    assert len(title_parser('')) == 6

def test_title_parser_parses_id():
    title = '42'
    title_id = '42'

    assert title_parser(title)['title_id'] == title_id

    title = '24'
    title_id = '24'

    assert title_parser(title)['title_id'] == title_id

def test_title_parser_converts_title_to_dict():

    correct_title_names = {
        '30 - Tape30 Side2 - L. Ron Hubbard 1.mp3': {
            'title_id': '30',
            'tape_number': '30',
            'side_id': 'B',
            'title': 'L. Ron Hubbard',
            'sub_chapter': '01',
            'file_type': 'mp3'
        },
        '30 - Tape10 Side1 - Battlefield Earth 20.mp4a': {
            'title_id': '30',
            'tape_number': '10',
            'side_id': 'A',
            'title': 'Battlefield Earth',
            'sub_chapter': '20',
            'file_type': 'mp4a'
        }
    }

    for input, output in correct_title_names.iteritems():
        assert title_parser(input) == output

def test_format_file():
    new_file = {
        'title_id': '30',
        'tape_number': '10',
        'side_id': 'A',
        'title': 'Battlefield Earth',
        'sub_chapter': '20',
        'file_type': 'mp4a'
    }

    expected_name = '10A20_Battlefield Earth.mp4a'

    assert filenamer(new_file) == expected_name

