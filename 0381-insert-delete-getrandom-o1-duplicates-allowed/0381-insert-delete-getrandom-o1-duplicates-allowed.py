class RandomizedCollection:
    def __init__(self):
        self.key_to_pos = dict()
        self.all_keys = list()


    def insert(self, val: int) -> bool:
        if val in self.key_to_pos:
            self.key_to_pos[val].add(len(self.all_keys))
            self.all_keys.append(val)
            return False
        else:
            self.key_to_pos[val] = set([len(self.all_keys)])
            self.all_keys.append(val)
            return True

    def remove(self, val: int) -> bool:
        if val in self.key_to_pos:
            pos = self.key_to_pos[val].pop()

            if len(self.key_to_pos[val]) == 0:
                del self.key_to_pos[val]

            if pos == len(self.all_keys) - 1:
                self.all_keys.pop()
                return True                

            if len(self.all_keys) == 1:
                self.all_keys = list()
                return True

            old_last_added_item_pos = len(self.all_keys) - 1
            last_added_item = self.all_keys.pop()
            self.all_keys[pos] = last_added_item

            self.key_to_pos[last_added_item].remove(old_last_added_item_pos)
            self.key_to_pos[last_added_item].add(pos)
            return True
        return False
        

    def getRandom(self) -> int:
        return random.choice(self.all_keys)
        
