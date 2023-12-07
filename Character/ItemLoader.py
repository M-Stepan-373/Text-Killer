import json

class ItemLoader:
    def __init__(self, item_file: str):
        self.content = None
        with open(item_file, 'r') as f:
            self.content = json.loads(f.read())
            
if __name__ == '__main__':
    loader = ItemLoader('./items.json')
    print(loader.content)
