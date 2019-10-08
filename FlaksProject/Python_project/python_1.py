import random
class Junde_Is_num:
    pass
is_num = 0
is_not_num = 0
def fun():
    """
    生成器：通常用于按照某种规律生成数，生成器内部不保存具体的数据，
        通常保存数据生成的规律。
    :return:
    """
    x=0
    global is_num,is_not_num
    while True:
        send_key= yield x
        if send_key.isalpha():
            is_num+=1
            print("全部是字母")
        else:
            is_not_num+=1
            print("不全是字母")

import random
example="abcd3dsafsj0920i1i312i3i21312l3j1lk23lk21j3lk21j3lkj21l3kj21l"
def get_stringf(k):
    f= fun()
    next(f)
    for i in range(k):
        string="".join(random.sample(example,5))
        print(string)
        f.send(string)
    print("全部是字母有【%s】个"%is_num)
    print("不全是字母有【%s】个"%is_not_num)

get_stringf(20)

