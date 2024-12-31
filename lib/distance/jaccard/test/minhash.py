import logging
logging.basicConfig(level=logging.DEBUG)

from ..data.test import elems, sets

from ..minhash import PermuteMinhash
def test_permute():
    permute_minhash = PermuteMinhash(elems, 5)
    
    minhashs = []
    
    logging.debug("elems: \n{}\n\npermutations: ".format(elems))
    
    for i in range(5):
        logging.debug("\n{}".format(permute_minhash.permutations[i]))
    
    logging.debug("\n")
    
    for i in range(len(sets)):
        minhashs.append(permute_minhash.calculate(sets[i]))
    
        logging.debug("set: {}\nminhash: {}".format(sets[i], minhashs[i]))

from ..minhash import HashMinhash
def test_hash():
    hash_minhash = HashMinhash(elems, 5)
    
    minhashs = []
    
    logging.debug("elems: \n{}\n\nhashs: ".format(elems))
    
    for i in range(5):
        logging.debug("\n{}".format(hash_minhash.hashs[i]))
    
    logging.debug("\n")
    
    for i in range(len(sets)):
        minhashs.append(hash_minhash.calculate(sets[i]))
    
        logging.debug("set: {}\nminhash: {}".format(sets[i], minhashs[i]))

# test_permute()
test_hash()

