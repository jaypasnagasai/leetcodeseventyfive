#841. Keys and Rooms

class Solution(object):
    def canVisitAllRooms(self, rooms):
        seen = [False] * len(rooms)
        seen[0] = True
        stack = [0]
        while stack:  #While we have keys...
            node = stack.pop() # get the next key 'node'
            for nei in rooms[node]: # For every key in room # 'node'...
                if not seen[nei]: # ... that hasn't been used yet
                    seen[nei] = True # mark that we've entered the room
                    stack.append(nei) # add the key to the todo list
        return all(seen) # Return true iff we've visited every room
