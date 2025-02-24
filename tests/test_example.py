from hexlet_pytest.example import reverse


def test_reverse():
    assert reverse('Hexlet') == 'telxeH'


def test_reverse_for_empty_string():
    assert reverse('') == ''

def test_stack():
    stack = []
    stack.append('one')
    stack.append('two')

    assert stack.pop() == 'two'
    assert stack.pop() == 'one'

def test_stack1():
    stack = []
    stack.append('one')
    stack.append('two')

    assert stack.pop() == 'two'

def test_stack2():
    stack = []
    stack.append('one')
    stack.append('two')

    stack.pop()
    assert stack.pop() == 'one'

def test_emptiness():
    stack = []
    assert not stack
    stack.append('one')
    assert bool(stack)  # not not stack

    stack.pop()
    assert not stack