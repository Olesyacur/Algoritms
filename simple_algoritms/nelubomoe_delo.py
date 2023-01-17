'''Вася размышляет, что ему можно не делать из того списка дел, который он
составил. Но, кажется, все пункты очень важные! Вася решает загадать число и
удалить дело, которое идёт под этим номером. Список дел представлен в виде
односвязного списка. Напишите функцию solution, которая принимает на вход
голову списка и номер удаляемого дела и возвращает голову обновлённого списка.

Формат ввода
Функция принимает голову списка и индекс элемента, который надо удалить
(нумерация с нуля). Список содержит не более 500 элементов. Список не бывает
пустым.
Формат вывода
Верните голову списка, в котором удален нужный элемент.'''

LOCAL = False

if LOCAL:
    class Node:  
        def __init__(self, value, next_item=None):  
            self.value = value  
            self.next_item = next_item


def solution(node, idx):
    def get_node_by_index(node, index):
        while index:
            node = node.next_item
            index -= 1
        return node

    if idx == 0:
        return node.next_item

    previous_node = get_node_by_index(node, idx-1)
    subsequent_node= get_node_by_index(node, idx+1) 
    previous_node.next_item = subsequent_node
    return node 

def test():
    node3 = Node("node3", None)
    node2 = Node("node2", node3)
    node1 = Node("node1", node2)
    node0 = Node("node0", node1)
    new_head = solution(node0, 1)
    assert new_head is node0
    assert new_head.next_item is node2
    assert new_head.next_item.next_item is node3
    assert new_head.next_item.next_item.next_item is None
    # result is node0 -> node2 -> node3

if __name__ == '__main__':
    test()