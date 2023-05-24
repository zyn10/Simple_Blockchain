import hashlib

def hashGenerator(data):
	result=hashlib.sha256(data.encode())
	return result.hexdigest()

class Block:
	def __init__(self,data,hash_,prev_hash):
		self.data=data
		self.hash_=hash_
		self.prev_hash=prev_hash

class Blockchain:
	def __init__(self):
		hashLast=hashGenerator('gen_last')
		hashStart=hashGenerator('gen_last')
	#Gensis Block
	genesis=Block('gen-data',hashLast,hashStart)
	self.chain=[genesis]


	def add_block(self,data):
		prev_hash = self.chain[-1].hash #last block ka hash
		hash = hashGenerator(data+prev_hash)
		newBlock=Block(data,hash,prev_hash)
		self.chain.append(newBlock)




obj=Blockchain()
obj.add_block('Z')
obj.add_block('A')
obj.add_block('I')
obj.add_block('N')


for block in obj.chain:
	print(block.dict)
