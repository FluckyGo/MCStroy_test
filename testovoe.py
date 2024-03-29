class TreeStore:
    def __init__(self, items) -> None:
        self.items: list[dict] = items

    def get_all(self) -> list[dict]:
        return self.items

    def get_item(self, id) -> dict | None:
        for item in self.items:
            if item.get('id') == id:
                return item

    def get_children(self, id: int) -> list:
        item_list: list = []
        for item in self.items:
            if item.get('parent') == id:
                item_list.append(item)
        return item_list

    def get_all_parents(self, id: int) -> list:
        parent_list: list = []
        item: dict = self.get_item(id)

        while item:
            parent_id: int = item.get('parent')
            if parent_id == 'root':
                break
            parent_item: dict = self.get_item(parent_id)
            parent_list.append(parent_item)
            self.get_all_parents(parent_id)
            item = parent_item
        return parent_list


ITEMS = [
    {"id": 1, "parent": "root"},
    {"id": 2, "parent": 1, "type": "test"},
    {"id": 3, "parent": 1, "type": "test"},
    {"id": 4, "parent": 2, "type": "test"},
    {"id": 5, "parent": 2, "type": "test"},
    {"id": 6, "parent": 2, "type": "test"},
    {"id": 7, "parent": 4, "type": None},
    {"id": 8, "parent": 4, "type": None}
]
ts = TreeStore(ITEMS)


ts.get_all()
assert ts.get_all() == ITEMS

ts.get_item(7)
assert ts.get_item(7) == ITEMS[-2]
assert ts.get_item(1) == ITEMS[0]
assert ts.get_item(8) == ITEMS[-1]

ts.get_children(4)
assert ts.get_children(4) == [{"id": 7, "parent": 4, "type": None},
                              {"id": 8, "parent": 4, "type": None}]
ts.get_children(5)
assert ts.get_children(5) == []
assert ts.get_children(1) == [{"id": 2, "parent": 1, "type": "test"},
                              {"id": 3, "parent": 1, "type": "test"},]
ts.get_all_parents(7)
assert ts.get_all_parents(7) == [{"id": 4, "parent": 2, "type": "test"},
                                 {"id": 2, "parent": 1, "type": "test"},
                                 {"id": 1, "parent": "root"}]
assert ts.get_all_parents(6) == [{"id": 2, "parent": 1, "type": "test"},
                                 {"id": 1, "parent": "root"}]
