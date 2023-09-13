from drugi_dan.iterator.node import Node

if __name__ == '__main__':
    #     1
    #    / \
    #   2   3
    #  /
    # 4
    # in-order: 213
    # preorder: 123
    # postorder: 231

    root = Node(1,
                Node(2, Node(4)),
                Node(3))
    #
    # _iter = iter(root)
    #
    # print([next(_iter).value for x in range(4)])

    for i in root:
        print(i.value)