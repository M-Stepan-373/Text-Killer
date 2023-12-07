import Character

class Inventory:
    '''Inventory component'''
    
    def __init__(self):
        self.items = []
        
    def add_item(self, item: Character.Item):
        self.items.append(item)
        
    def delete_item(self, item: Character.Item):
        for ind, it in enumerate(self.items):
            if it == item:
                self.items.pop(ind)
                return it
