from collections import deque
from Block import Block
from Map import Map


def print_stack(st):
    for b in st:
        print(b, end = ' ')
    print()

class DepthFirstSearch:
    def __init__(self, map: Map) -> None:
        self.stack = []
        self.path = dict()
        self.visited = set()
        self.solution = []
        self.map = map 

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
                print_stack(solution)
                return True, list(reversed(solution))

            prev_state = u.deepcopy()
            cur = u
            done = False
            print('-left')
            temp = cur.move_left(self.map)
            self.sub_process(prev_state, temp)

            print('--right')
            temp = cur.move_right(self.map)
            self.sub_process(prev_state, temp) 

            print('---up')
            temp = cur.move_up(self.map)
            self.sub_process(prev_state, temp)

            print('---down')
            temp = cur.move_down(self.map)
            self.sub_process(prev_state, temp)
            if done:
                return True, self.solution

        return False, []

    def sub_process(self, prev_state, v):
        success = not (prev_state.encode() == v.encode())
        # print("sub process:",self.visited)
        encode = v.encode()
        if success and (encode not in self.visited):
            self.stack.append(v)
            self.path[encode] = prev_state 
            self.visited.add(encode)
        # return False

    def is_goal(self, block):
        return self.map.impact(block) == 2
