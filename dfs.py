import copy
from Block import Block
from Map import Map


class DepthFirstSearch:

    def __init__(self, map: Map) -> None:
        self.stack = []
        self.path = dict()
        self.visited = set()
        self.solution = []
        self.map = map 
        self.moves = ["move_left", "move_right", "move_up", "move_down"]

    def solve(self, src : Block) :
        self.stack.append(src)
        self.visited.add(src.encode())
        while len(self.stack) > 0:
            u = self.stack.pop()
            if self.is_goal(u):
                solution = []
                while u is not None:
                    solution += [u]
                    if u.encode() in self.path:
                        u = self.path[u.encode()]
                    else:
                        break
                    
                solution.reverse()
                self.print_stack(solution)
                return True, list(solution)

            prev_state = copy.deepcopy(u)
            
            for move_name in self.moves:
                print(move_name, end = "---\n")
                move = getattr(Block, move_name)
                move(u)
                if not self.is_failed(u):
                    encode = u.encode()
                    if encode not in self.visited:
                        self.stack.append(u)
                        self.path[encode] = prev_state
                        self.visited.add(encode)
                u = copy.deepcopy(prev_state)

        return False, []

    def is_goal(self, block):
        return self.map.won_the_game(block)

    def is_failed(self, block):
        return self.map.block_out_map(block) or self.map.block_felt(block)

    @staticmethod
    def print_stack(st):
        for b in st:
            print(b, end=' ')
        print()