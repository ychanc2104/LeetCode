

x = 10
y = 100


def test_global():
    # get x outside of test_global
    global x
    print('test_global before re-assign x:', x)
    # change x variable from 10 to 11
    x = 11
    print('test_global x:',x)

def test_nonlocal():
    y = 101

    def sub():
        # use y outside of sub()
        nonlocal y
        print('sub before re-assign y:', y)
        # only affect in test_nonlocal()
        y = 102
        print('sub y:', y)
    sub()
    print('test_nonlocal y:',y)

test_global()

test_nonlocal()