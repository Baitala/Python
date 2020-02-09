import Lecture_13

def is_braces_sequence_correct(s: str):
    '''
    Verify correctness of bracket sequence with round and square brackets () []
    '''

    for brace in s:
        if brace not in '()[]':
            continue
        if brace in '([':
            Lecture_13.push(brace)
        else:
            assert brace in ')]', 'Closing bracket expected: ' + str(brace)
            if Lecture_13.is_empty():
                return False
            left = Lecture_13.pop()
            assert left in '([', 'Opening bracket expected: ' + str(brace)
            if left == '(':
                right = ')'
            elif left == '[':
                right = ']'
            if right != brace:
                return False
    return Lecture_13.is_empty()

