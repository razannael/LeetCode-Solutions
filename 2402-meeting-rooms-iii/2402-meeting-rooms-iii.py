class Solution:
    def mostBooked(self, num_rooms, meetings):
        # Create a list of available rooms using indices from 0 to num_rooms-1
        available_rooms = [room for room in range(num_rooms)]
        occupied_rooms = []  # Stores rooms that are currently occupied
        heapify(available_rooms)  # Convert the available_rooms list into a heap
        booking_counts = [0] * num_rooms  # Initialize a list to keep track of booking counts per room

        # Sort the meetings in ascending order based on the start time
        sorted_meetings = sorted(meetings, key=lambda x: x[0])
        for start_time, end_time in sorted_meetings:
            # Check if there are any available rooms at the start time of the meeting
            while occupied_rooms and occupied_rooms[0][0] <= start_time:
                # Room becomes available, add it back to the available_rooms heap
                end, room = heappop(occupied_rooms)
                heappush(available_rooms, room)

            if available_rooms:
                # Assign an available room from the available_rooms heap to the meeting
                room = heappop(available_rooms)
                heappush(occupied_rooms, [end_time, room])  # Add the meeting to the occupied_rooms heap
            else:
                # All rooms are occupied, find the room with the earliest end time
                current_end, room = heappop(occupied_rooms)
                new_end = current_end + end_time - start_time  # Update the room's end time
                heappush(occupied_rooms, [new_end, room])

            booking_counts[room] += 1  # Increment the booking count for the assigned room

        # Find the room with the maximum booking count and return its index
        max_booking_count = max(booking_counts)
        most_booked_room = booking_counts.index(max_booking_count)
        return most_booked_room





