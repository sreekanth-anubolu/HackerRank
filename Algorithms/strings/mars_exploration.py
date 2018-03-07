#!/bin/python3

import math

def marsExploration(received_sos_message):
    sos_message_reference = "SOS"
    _index_jump = len(sos_message_reference)
    _count = len(received_sos_message) / _index_jump
    _start = 0
    _end = _index_jump

    _corrupted_count = 0
    for n in range(int(_count)):
        if n > 0:
            _start = _start + _index_jump
            _end = _end + _index_jump

        _msg = received_sos_message[_start: _end]
        if _msg[0] != sos_message_reference[0]:
                _corrupted_count += 1

        if _msg[1] != sos_message_reference[1]:
                _corrupted_count += 1

        if _msg[2] != sos_message_reference[2]:
                _corrupted_count += 1

    return _corrupted_count


if __name__ == "__main__":
    s = input().strip()
    result = marsExploration(s)
    print(result)


