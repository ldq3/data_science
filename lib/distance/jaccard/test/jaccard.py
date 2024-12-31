from ..data.test import elems, sets, res

from ..mod import Jaccard
def test_jaccard():
    jaccard = Jaccard
    
    for i in range(len(sets)):
        for j in range(len(sets)):
            assert jaccard.similarity(sets[i], sets[j]) == res[i][j]

from ..mod import MinhashJaccard

from ..minhash import PermuteMinhash
def test_minhash():
    minhash_jaccard = MinhashJaccard(PermuteMinhash(elems, 5))
    
    for i in range(len(sets)):
        for j in range(len(sets)):
            minhash_jaccard.similarity(sets[i], sets[j])

test_minhash()
