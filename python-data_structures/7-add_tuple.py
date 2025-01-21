#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a_tuple1, a_tuple2 = (tuple_a + (0, 0))[:2]
    b_tuple1, b_tuple2 = (tuple_b + (0, 0))[:2]

    my_tuple = (a_tuple1 + b_tuple1, a_tuple2 + b_tuple2)

    return (my_tuple)
