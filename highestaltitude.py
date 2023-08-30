#1732. Find the Highest Altitude

class Solution:
    def largestAltitude(self, gain):
        current_altitude = 0
        # Initialize the highest altitude to the starting altitude, which is 0.
        highest_point = current_altitude
        
        # Loop through each altitude gain value.
        for altitude_gain in gain:
            # Add the altitude gain to the current altitude.
            current_altitude += altitude_gain
            # Check if the current altitude surpasses the previously recorded highest altitude.
            highest_point = max(highest_point, current_altitude)
        
        # Return the highest altitude reached during the journey.
        return highest_point
