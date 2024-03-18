# Тестовое задание для ООО "МСтрой" 

# ЗАДАНИЕ
Есть массив объектов, которые имеют поля id и parent, через которые их можно связать в дерево и некоторые произвольные поля.

# Нужно написать класс, который принимает в конструктор массив этих объектов и реализует 4 метода:
   - get_all() Должен возвращать изначальный массив элементов.
   - get_item(id) Принимает id элемента и возвращает сам объект элемента;
   - get_children(id) Принимает id элемента и возвращает массив элементов, являющихся дочерними для того элемента, чей id получен в аргументе. Если у элемента нет дочерних, то должен возвращаться пустой массив;
   - get_all_parents(id) Принимает id элемента и возвращает массив из цепочки родительских элементов, начиная от самого элемента, чей id был передан в аргументе и до корневого элемента, т.е. должен получиться путь элемента наверх дерева через цепочку родителей к корню дерева. Порядок элементов важен!

# Требования: максимальное быстродействие, следовательно, минимальное количество обходов массива при операциях, в идеале, прямой доступ к элементам без поиска их в массиве.


# Примеры использования:
```
 - ts.get_all() // [
                     {"id":1,"parent":"root"},
                     {"id":2,"parent":1,"type":"test"},
                     {"id":3,"parent":1,"type":"test"},
                     {"id":4,"parent":2,"type":"test"},
                     {"id":5,"parent":2,"type":"test"},
                     {"id":6,"parent":2,"type":"test"},
                     {"id":7,"parent":4,"type":None},
                     {"id":8,"parent":4,"type":None}
                   ]

 - ts.get_item(7) // {"id":7,"parent":4,"type":None}

 - ts.get_children(4) // [
                             {"id":7,"parent":4,"type":None},
                             {"id":8,"parent":4,"type":None}
                         ]

 - ts.get_children(5) // []

 - ts.get_all_parents(7) // [
                                 {"id":4,"parent":2,"type":"test"},
                                 {"id":2,"parent":1,"type":"test"},
                                 {"id":1,"parent":"root"}
                             ]
```
