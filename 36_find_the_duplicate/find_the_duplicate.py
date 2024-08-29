def find_the_duplicate(nums):
    """Find duplicate number in nums.

    Given a list of nums with, at most, one duplicate, return the duplicate.
    If there is no duplicate, return None

        >>> find_the_duplicate([1, 2, 1, 4, 3, 12])
        1

        >>> find_the_duplicate([6, 1, 9, 5, 3, 4, 9])
        9

        >>> find_the_duplicate([2, 1, 3, 4]) is None
        True
    """
    seen = set()

    for number in nums:
        if number in seen:
            return number  # Return the duplicate number
        seen.add(number)  # Add the number to the set if not seen before

    return None  # Return None if no duplicate is found (should not happen in this case)

    

    # from collections import Counter

    # def find_duplicate(numbers):
    #     # Create a Counter object to count occurrences of each number
    #     counts = Counter(numbers)
        
    #     # Find the element with a count greater than 1
    #     for number, count in counts.items():
    #         if count > 1:
    #             return number

    #     return None  # Return None if no duplicate is found (should not happen in this case)

    # # Example list
    # my_list = [1, 2, 3, 4, 5, 3]

    # # Find and print the duplicate number
    # duplicate = find_duplicate(my_list)
    # print(duplicate)  # Output: 3