from hashlib import sha256
from typing import List

def hash(data:bytes)->bytes:
    return sha256(data).digest()


def hash_leaves(leaft:bytes,right:bytes)->bytes:
    return hash(leaft+right)

class MerkleTree:
    def __init__(self,leaves:List[bytes]):
        self.tree=self.compute_tree(leaves)

    def root(self)->bytes:
        return self.tree[-1][0]
    
    def compute_tree(self,leaves:List[bytes])->bytes:
        if len(leaves)%2!=0: #如果不是偶数,则补充一个0节点
            leaves.append(hash(b"0"))
        tree=[leaves] #tree是一个二维矩阵

        while len(leaves)!=1: #当前这一层节点不是1，就继续往上计算
            #使用步长为2的循环，把相邻的两个节点i和i+1调用hash_leaves合并成一个新的哈希值
            leaves=[hash_leaves(leaves[i],leaves[i+1]) for i in range(0,len(leaves),2)]
            if len(leaves)%2!=0 and len(leaves)!=1: #如果没到顶层且节点数又是奇数，则再加一个0
                leaves.append(hash(b"0"))
            tree.append(leaves) #[[A,B,C,D],[AB_hash,CD_hash],[Root]]
        return tree
    
    def proof(self,leaf_index:int)->bytes:
        proof=[]
        for i in range(len(self.tree)-1): #遍历树的每一层
            if leaf_index%2==0: #如果索引是偶数，说明在左边
                proof.append((0,self.tree[i][leaf_index+1])) #告诉Verifier左节点的兄弟在右边(索引+1)
            else: #索引是奇数，是右节点
                proof.append((1,self.tree[i][leaf_index-1])) #告诉Verifier右节点的兄弟在左边(索引-1)
            leaf_index //=2 #寻找父节点
        return proof #假设从leaf_index=1开始,proof=[(1,A_hash),(0,Hash(CD))]
        '''
                Root
               /    \ 
            AB      CD
           /  \    /  \ 
          A    B  C    D
        '''
    
    #通过叶子节点和path上的proof不断向上求哈希，最终计算出这棵树的Root Hash
    @staticmethod
    def compute_tree_from_proof(leaf:bytes,proof:List[bytes])->bytes:
        leaf=hash(leaf) #计算树底层的第一个hash节点

        for(direction,sibling) in proof: 
            if direction==0: #如果是0，则说明当前的leaf是左节点,然后进行哈希
                leaf=hash_leaves(leaf,sibling)
            else: #如果是1，则说明当前是右节点
                leaf=hash_leaves(sibling,leaf)
        return leaf #最终返回根节点
    
def test():
    leaves=[
        b'123',
        b'456',
        b'789',
        b'1011',
    ]
    hashed=[hash(leaf)for leaf in leaves]
    mt=MerkleTree(hashed) #返回Merkle Tree
    print(mt.root().hex())
    proof=mt.proof(0) #从节点0开始计算path_proof
    print(mt.compute_tree_from_proof(leaves[0], proof).hex())
    

test()
