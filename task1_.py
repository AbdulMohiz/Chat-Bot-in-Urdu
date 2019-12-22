# List of questions-answers in the form of array, we can call either question/answer
# by using their indexes.
# by Abdul Mohiz


def array_questions():
    mylist = []
    list1 = []
    list2 = []
    q = []
    a = []
    final = []
    with open("corpora.txt", 'r', encoding='utf-8') as f:
        for line in f.readlines():
            mylist = line.strip().split("|")
            list1.append(mylist[0])
            list2.append(mylist[1])
            final = list1 + list2
    return final
