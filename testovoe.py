from pprint import pprint

# ЗАДАНИЕ
# Есть массив объектов, которые имеют поля id и parent, через которые их можно связать в дерево и некоторые произвольные поля.

# Нужно написать класс, который принимает в конструктор массив этих объектов и реализует 4 метода:
#   - getAll() Должен возвращать изначальный массив элементов.
#   - getItem(id) Принимает id элемента и возвращает сам объект элемента;
#   - getChildren(id) Принимает id элемента и возвращает массив элементов, являющихся дочерними для того элемента, чей id получен в аргументе. Если у элемента нет дочерних, то должен возвращаться пустой массив;
#   - getAllParents(id) Принимает id элемента и возвращает массив из цепочки родительских элементов, начиная от самого элемента, чей id был передан в аргументе и до корневого элемента,
#  т.е. должен получиться путь элемента наверх дерева через цепочку родителей к корню дерева. Порядок элементов важен!

# Требования: максимальное быстродействие, следовательно, минимальное количество обходов массива при операциях, в идеале, прямой доступ к элементам без поиска их в массиве.


class TreeStore:
    def __init__(self, items) -> None:
        self.items = items

    def getAll(self):
        return self.items

    def getItem(self, id):
        for item in items:
            if item.get('id') == id:
                return item

    def getChildren(self, id):
        item_list = []
        for item in items:
            if item.get('parent') == id:
                item_list.append(item)
        return item_list

    def getAllParents(self, id):
        parent_list = []
        starter = True
        while starter:
            starter = False
            for item in items:
                if item.get('id') == id:
                    pprint(item)


items = [
    {"id": 1, "parent": "root"},
    {"id": 2, "parent": 1, "type": "test"},
    {"id": 3, "parent": 1, "type": "test"},
    {"id": 4, "parent": 2, "type": "test"},
    {"id": 5, "parent": 2, "type": "test"},
    {"id": 6, "parent": 2, "type": "test"},
    {"id": 7, "parent": 4, "type": None},
    {"id": 8, "parent": 4, "type": None}
]
ts = TreeStore(items)


# pprint(ts.getAll())
# assert ts.getAll() == items

# pprint(ts.getItem(7))
# assert ts.getItem(7) == items[-2]
# assert ts.getItem(1) == items[0]
# assert ts.getItem(8) == items[-1]

# pprint(ts.getChildren(4))
# assert ts.getChildren(4) == [{"id": 7, "parent": 4, "type": None},
#                              {"id": 8, "parent": 4, "type": None}]
# pprint(ts.getChildren(5))
# assert ts.getChildren(5) == []
# assert ts.getChildren(1) == [{"id": 2, "parent": 1, "type": "test"},
#                              {"id": 3, "parent": 1, "type": "test"},]
pprint(ts.getAllParents(7))


# Примеры использования:
#  - ts.getAll() // [{"id":1,"parent":"root"},{"id":2,"parent":1,"type":"test"},{"id":3,"parent":1,"type":"test"},{"id":4,"parent":2,"type":"test"},{"id":5,"parent":2,"type":"test"},{"id":6,"parent":2,"type":"test"},{"id":7,"parent":4,"type":None},{"id":8,"parent":4,"type":None}]
#
#  - ts.getItem(7) // {"id":7,"parent":4,"type":None}
#
#  - ts.getChildren(4) // [{"id":7,"parent":4,"type":None},{"id":8,"parent":4,"type":None}]
#  - ts.getChildren(5) // []
#
#  - ts.getAllParents(7) // [{"id":4,"parent":2,"type":"test"},{"id":2,"parent":1,"type":"test"},{"id":1,"parent":"root"}]
