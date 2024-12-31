from abc import ABC, abstractmethod
import random

class Minhash(ABC):
    @abstractmethod
    def calculate(self, set1):
        """生成目标集合的 minhash 签名

        Args:
            set1 (set): 目标集合
        
        Returens:
            list: set1 的 minhash 签名
        """
        pass

class PermuteMinhash(Minhash):
    def __init__(self, elems, num):
        """基于随机排列的 minhash 签名

        Args:
            elems (list): 集合的基本元素
            num (int): minhash 签名的长度
        """
        self.elems = elems
        
        self.permutations = []
        for _ in range(num):
            self.permutations.append(random.sample(range(len(elems)), len(elems)))
        
    def calculate(self, set1):
        signature = [ ]

        for i in range(len(self.permutations)):
            for index in self.permutations[i]:
                if self.elems[index] in set1:
                    signature.append(index)
                    break

        return signature

class HashMinhash(Minhash):
    def __init__(self, elems, num):
        """基于哈希函数模拟随机排列的 minhash 签名

        Args:
            elems (list): 集合的基本元素
            num (int): minhash 签名的长度
        """
        self.elems = elems
        
        self.hashs = []
        for _ in range(num):
            a = random.randint(1, len(elems))
            b = random.randint(1, len(elems))
            self.hashs.append((a, b))
            
    def calculate(self, set1):
        signature = []

        for i in range(len(self.hashs)):
            (a, b) = self.hashs[i]
            
            hashed_minimum = len(self.elems)
            candidate_index = len(self.elems)
            
            for index in range(len(self.elems)):
                hashed_index = (a * index + b) % len(self.elems)
                if (hashed_index < hashed_minimum) and (self.elems[index] in set1):
                    hashed_minimum = hashed_index
                    candidate_index = index

            signature.append(candidate_index)

        return signature
