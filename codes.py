import enum

class Codes(enum.IntEnum):
    sort_up = 1
    sort_down = 2
    shuffle = 3
    sort_len_up = 4
    sort_len_down = 5

class Error_codes(enum.IntEnum):
    ok = 200
    no_file = 404
    bad_request = 400
