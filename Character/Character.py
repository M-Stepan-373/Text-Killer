from Character import Inventory

class Character:
    '''Character entity'''

    def __init__(self, *, nickname: str, inventory: Inventory):
        self.hp = 100
        
        self.nickname = nickname
        self.inventory = inventory
