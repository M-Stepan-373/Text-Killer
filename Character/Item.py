class Item:
    '''Base item component'''
    
    def __init__(self, max_strength: int):
        self.strength = max_strength
        self.max_strength = max_strength
