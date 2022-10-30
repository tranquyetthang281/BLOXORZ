from Solution import Solution
from Map import Map
from Block import Block
import copy

class GeneticAlgorithm(Solution):
    
    def __init__(self, map: Map) -> None:
        super().__init__(map)

    def solve(self, src : Block) :
        return False, []
