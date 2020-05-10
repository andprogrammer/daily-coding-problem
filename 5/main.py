def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

def car(pair):
    def first_arg(a, b):
        return a
    return pair(first_arg)

def cdr(pair):
    def second_arg(a, b):
        return b
    return pair(second_arg)

if __name__ == '__main__':
    assert car(cons(3, 4)) == 3
    assert cdr(cons(3, 4)) == 4
