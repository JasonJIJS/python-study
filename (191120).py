
if __name__ == "__main__":
    tuple1 = (1, 2, 3, 4)
    print("tuple1 {} type : {}".format(tuple1, type(tuple1)))

    tuple2 = 5, 6, 7, 8
    print("tuple2 {} type : {}".format(tuple2,type(tuple2)))

    tuple3 = (9, )
    tuple4 = 10,
    print("tuple3 {} type : {}".format(tuple3, type(tuple3)))
    print("tuple4 {} type : {}".format(tuple4, type(tuple4)))

    t_list = [tuple1, tuple2, tuple3, tuple4]
    for t in t_list[0:len(t_list):1]:
        print("{} type : {}".format(t, type(t)))

    # tuple[1] = 5   에러난다, 리스트랑 다른 튜플
    # tuple1 = (1, 2, 3, 4)
    print(len(tuple1))
    print(tuple1[1])
    print(tuple1[1] + tuple1.index(2))
    print("{}, {}".format(tuple1[1], tuple1.index(2)))



