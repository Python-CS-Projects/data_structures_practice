class BS:

    def binarySearch(self, sorted_array, target):
        # LOW pointer
        low = 0
        # HIGH pointer
        high = len(sorted_array) - 1
        # Midpoint 1/2 of array
        midpoint = (high - low) // 2

        # Check IF TARGET is == Midpoint
        if target == sorted_array[midpoint]:
            # Return midpoint
            return midpoint
        # ELIF Target < midpoint value
        elif target < sorted_array[midpoint]:
            # Recursive case on left side
            return self.binarySearch(sorted_array[:midpoint],target)
        # Else
        else:
            # Recursive case on right side
            return self.binarySearch(sorted_array[midpoint:],target)


bs = BS()

arr = [1,2,3,4,5,6,7,8,9]
x = bs.binarySearch(arr,2)
print(f"Found at index: {x}")