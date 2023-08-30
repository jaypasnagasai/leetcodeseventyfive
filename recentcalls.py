#933. Number of Recent Calls

class RecentCounter:
    def __init__(self):
        # Initialize a deque to serve as the sliding window.
        self.slide_window = deque()

    def ping(self, t):
        # Step 1: Append the current ping time to the sliding window.
        self.slide_window.append(t)

        # Step 2: Remove outdated pings (older than 3000 milliseconds).
        while self.slide_window[0] < t - 3000:
            self.slide_window.popleft()  # Remove the leftmost (oldest) ping.

        # Return the count of pings within the last 3000 milliseconds.
        return len(self.slide_window)
