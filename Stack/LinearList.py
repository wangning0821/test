# 王宁
# 开发时间：2023/5/4 22:58


class Mysqlist:
    def __init__(self, size):
        self.size = size
        self.sqlist = []

    def listinsert(self, i, x):
        if i < 1 or i > self.size:
            print("Insert Location Error！")
            return False
        else:
            self.sqlist.insert(i, x)
            return True

    def listdelete(self, i):
        if i < 1 or i > self.size:
            print("Delete Location Error！")
            return False
        else:
            self.sqlist.pop(i)
            return False

    def findelem(self, i):
        if i < 1 or i > self.size:
            print("search Location Error！")
            return False
        else:
            return self.sqlist[i]

    def showlist(self):
        return self.sqlist


# 定义节点
class Node:
    # 初始化
    def __init__(self, value):
        # value存放数据元素
        self.value = value
        # next是下一个节点的标识
        self.next = None


class LinkList:
    def __init__(self):
        self._head = None

    def is_empty(self):
        return self._head is None

    def length(self):
        lt = 0
        current = self._head
        while current is not None:
            lt += 1
            current = current.next
        return lt

    # 遍历链表
    def items(self):
        current = self._head
        while current is not None:
            yield current.value
            current = current.next

    # 向链表头部添加元素
    def insert_head(self, value):
        new_node = Node(value)
        new_node.next = self._head
        self._head = new_node

    # 尾部添加元素
    def append(self, value):
        new_node = Node(value)
        if self.is_empty():
            self._head = new_node
        else:
            current = self._head
            while current.next is not None:
                current = current.next
            current.next = new_node

    # 指定位置插入元素
    def insert_index(self, index, value):

        if index <= 0:
            self.insert_head(self, value)
        elif index > (self.length() - 1):
            self.append(value)
        else:
            new_node = Node(value)
            current = self._head
            for _ in range(index-1):
                current = current.next
            new_node.next = current.next
            current.next = new_node

        # 删除节点
    def remove(self, value):
        current = self._head
        pre = None
        while current is not None:
            if current.value == value:
                if not pre:
                    self._head = current.next
                else:
                    pre.next = current.next
                return True
            else:
                pre = current
                current = current.next

    # 查找元素是否存在
    def find(self, value):
        return value in self.items()


if __name__ == "__main__":
    link_list = LinkList()
    node1 = Node(1)
    node2 = Node(2)
    link_list._head = node1
    node1.next = node2
    print(link_list._head.value)
    print(link_list._head.next.value)
    print(link_list.is_empty())
    print(link_list.length())
    for t in range(7):
        link_list.append(t)
    link_list.insert_head(10)
    print(link_list.length())
    print(list(link_list.items()))
    link_list.insert_index(3, 20)
    print(list(link_list.items()))
    print(link_list.find(10))
    link_list.remove(2)
    print(list(link_list.items()))


