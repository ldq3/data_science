elems = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

sets = [
    {'a', 'e', 'k', 'p', 'z'}, 
    {'b', 'g', 'm', 's', 't'},
    {'c', 'd', 'f', 'h', 'j'},
    {'l', 'n', 'q', 'r', 'w'},
    {'i', 'o', 'u', 'v', 'x'},
    {'y', 'z', 'a', 'b', 'c'}
]

res = [
    [1, 0, 0, 0, 0, 2/8],
    [0, 1, 0, 0, 0, 1/9],
    [0, 0, 1, 0, 0, 1/9],
    [0, 0, 0, 1, 0, 0], 
    [0, 0, 0, 0, 1, 0],
    [2/8, 1/9, 1/9, 0, 0, 1]
]