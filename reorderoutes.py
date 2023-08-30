#1466. Reorder Routes to Make All Paths Lead to the City Zero

class Solution:
    def minReorder(self, n, connections):
        A, B = collections.defaultdict(list), collections.defaultdict(list)
        for a, b in connections:
            A[b].append(a)
            B[a].append(b)
        result, stack, visited = 0, [0], {0}
        while stack:
            city = stack.pop()
            if city in A:
                for x in A[city]:
                    if x in visited:
                        continue
                    stack.append(x)
                    visited.add(x)
            if city in B:
                for x in B[city]:
                    if x in visited:
                        continue
                    result += 1
                    stack.append(x)
                    visited.add(x)
    
        return result
