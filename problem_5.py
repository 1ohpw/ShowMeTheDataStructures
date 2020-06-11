import hashlib
import time

class Block:
    def __init__(self, data, previous_hash):
        self.timestamp = time.strftime("%a, %d %b %Y %I:%M:%S %p %Z", time.gmtime())
        self.data = data
        self.data_with_prev = data + previous_hash
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()
        self.next = None
    
    def calc_hash(self):
        sha = hashlib.sha256()
        hash_str = self.data_with_prev.encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()
    
    def get_hash(self):
        return self.hash
    
    def set_previous_hash(self, hash_code):
        self.previous_hash = hash_code

class BlockChain:
    def __init__(self):
        self.genesis_block = None
        self.previous_block = None
    
    def add_block(self, data):
        if data:
            previous_hash = ""
            if self.previous_block:
                previous_hash = self.previous_block.get_hash()

            new_block = Block(data, previous_hash)

            if self.genesis_block == None:
                self.genesis_block = new_block
                self.previous_block = self.genesis_block
                return

            if self.previous_block:
                self.previous_block.next = new_block
        
            self.previous_block = new_block
    
    #for testing
    def print_blocks(self):
        current_block = self.genesis_block
        i = 1
        while current_block:
            print("Block #" + str(i) + " Hash: " + current_block.get_hash())
            current_block = current_block.next
            i += 1

#Test Case 1
# block_chain = BlockChain()
# block_chain.add_block("Wolf")
# block_chain.add_block("Mann")
# block_chain.add_block("Jack")
# block_chain.print_blocks()
#expected --> printing the hases of each block in order. 
#changing the data string of one block should change its hash
#as well as the hashes of every Block following it in the chain. 

#Test Case 2
# block_chain2 = BlockChain()
# block_chain2.add_block("Genesis")
# block_chain2.add_block("")
# block_chain2.print_blocks()
#expected --> printing of just the genesis block hash

#Test Case 3
# block_chain3 = BlockChain()
# block_chain3.add_block(None)
# block_chain3.print_blocks()
#expected ---> nothing

#Test Case 4
# block_chain4 = BlockChain()
# data_str = "a"
# for _ in range(0, 1000):
#     block_chain4.add_block(data_str)
#     data_str += "a"
# block_chain4.print_blocks()
#expected ---> the hashes of 1000 blocks