#735. Asteroid Collision

class Solution:
    def asteroidCollision(self, asteroids):
        stack = []

        for a in asteroids:
            if a > 0:
                # Current asteroid is moving to the right, so add it to the stack.
                stack.append(a)
            else:  # a < 0
                # Current asteroid is moving to the left (negative direction).

                # Check for collisions with previous positive asteroids in the stack.
                while stack and stack[-1] > 0 and stack[-1] < -a:
                    stack.pop()  # Destroy previous positive asteroid(s) that will collide.

                if not stack or stack[-1] < 0:
                    stack.append(a)  # If stack is empty or top asteroid is also negative, add the current asteroid.
                elif stack[-1] == -a:
                    stack.pop()  # Both the current negative asteroid and the top positive asteroid will collide and destroy each other.
                else:  # stack[-1] > current
                    pass  # The current negative asteroid is destroyed by the top positive asteroid.

        return stack  # Return the remaining asteroids in the stack after all collisions have been resolved.
