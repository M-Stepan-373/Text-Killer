import Character

class InventoryManager:
    @staticmethod
    def take_item(item: Character.Item, entity: Character):
        entity.inventory.add_item(item)
        
    @staticmethod
    def put_item(item: Character.Item, entity: Character):
        entity.inventory.delete_item(item)
