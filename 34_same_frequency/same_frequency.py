def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """

    sorted_num1 = int(''.join(sorted(str(num1), reverse=True)))
    sorted_num2 = int(''.join(sorted(str(num2), reverse=True)))

    return sorted_num1 == sorted_num2