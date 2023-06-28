#!/usr/bin/python3

"""
7. Singly linked list
"""


class Node:
    """
    Node

    Args:
        data (int): value to set as data
        next_node (Node): node to set
    Raises:
        TypeError: If data is not an integer
    """
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        data gettter

        Returns:
            int: Node integer data
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        data setter

        Args:
            value (int): value to set as data
        Raises:
            TypeError: If value is not an integer
        """
        if type(value) != int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """
        next_node gettter

        Returns:
            Node: next node
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        next_node setter

        Args:
            value (Node): node to set
        Raises:
            TypeError: If value is not a Node object
        """
        if type(value) != Node and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """
    defines a singly linked list
    """
    def __init__(self):
        self.__head: Node | None = None

    def sorted_insert(self, value):
        """
        inserts a new Node into the correct sorted position in the list
        (increasing order)

        Args:
            value (int): integer value to add
        Raises:
            TypeError: If value is not an integer
        """
        node = Node(value)
        if self.__head is None:
            self.__head = node
        else:
            cur = self.__head
            old = None
            while cur.data <= node.data and cur.next_node is not None:
                old = cur
                cur = cur.next_node
            node.next_node = cur
            if cur.data <= node.data:
                cur.next_node = node
                node.next_node = None
            else:
                if old is not None:
                    old.next_node = node
                else:
                    self.__head = node

    def __str__(self) -> str:
        """
        returns string version of SinglyLinkedList
        """
        val = ""
        node = self.__head
        while node is not None:
            val += f"{node.data}"
            node = node.next_node
            if node is not None:
                val += "\n"
        return val


if __name__ == "__main__":
    sll = SinglyLinkedList()
    sll.sorted_insert(2)
    sll.sorted_insert(5)
    sll.sorted_insert(3)
    sll.sorted_insert(10)
    sll.sorted_insert(1)
    sll.sorted_insert(-4)
    sll.sorted_insert(-3)
    sll.sorted_insert(4)
    sll.sorted_insert(5)
    sll.sorted_insert(12)
    sll.sorted_insert(3)
    print(sll)
