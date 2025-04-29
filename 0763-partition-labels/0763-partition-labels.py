class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # Create a dictionary to store the last occurrence index of each character
        last_occurence = {}

        for i , char in enumerate(s):
            last_occurence[char] = i
        
        # Initialize variables to track partition boundaries
        result = []
        start = 0
        end = 0

        # Iterate through the string to find partitions
        for i , char in enumerate(s):

            # Expand the current partition's end if needed
            end = max(end , last_occurence[char])


            # If we've reached the end of the current partition
            if i == end:

                # Calculate partition length and add to result
                partition_length = end - start + 1
                result.append(partition_length)

                # Update start for the next partition
                start = i + 1

        return result
