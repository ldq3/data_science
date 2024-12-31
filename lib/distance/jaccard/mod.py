from abc import ABC, abstractmethod

class Jaccard(ABC):
    @abstractmethod
    def similarity(self, set1, set2):
        """计算两个集合的 Jaccard 相似度
        
        Args:
            set1 (set): 第一个集合
            set2 (set): 第二个集合
        
        Returns:
            set1 和 set2 的 Jaccard 相似度
        """
        intersection = set1.intersection(set2)
        union = set1.union(set2)

        return len(intersection) / len(union)

    def distance(self, set1, set2):
        """计算两个集合的 Jaccard 距离
    
        参数：
            set1: 第一个集合
            set2: 第二个集合
        
        返回：
            set1 和 set2 的 Jaccard 距离
        """
        return 1 - self.similarity(set1, set2)

from .minhash import Minhash
class MinhashJaccard(Jaccard):
    def __init__(self, minhash: Minhash):
        self.minhash = minhash
    
    def similarity(self, set1, set2):
        signature1 = self.minhash.calculate(set1)
        signature2 = self.minhash.calculate(set2)
        
        length = len(signature1)
        
        counter = 0
        for i in range(length):
            if signature1[i] == signature2[i]:
                counter += 1
        
        similarity = counter / length
        
        return similarity
