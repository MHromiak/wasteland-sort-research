from typing import Union

def wasteland_sort(landmarks: list, reverse: bool) -> list:
    """ O(m+n) integer sorting algorithm developed with the intent of providing better performance than widely-used sorts 
    in terms of both memory and time for integer sorting. Currently runs in O(m_n) time and O(max(m, n)) space.
    
    Parameters
    ----------
    landmarks: List[int]
        List of integers to be sorted
    
    reverse: bool
        True if you want to sort integers in reverses

    
    Returns
    -------
    Pseudo in-place landmarks array. Each value is actually replaced with another integer.
    """
    if landmarks == [] or len(landmarks) == 1:
        return landmarks
    least, most = find_extremes(landmarks)

    wasteland: list = [0] * (most - least + 1)

    for value in landmarks:
        index = value - least
        wasteland[index] += 1

    index: int = 0
    num_sorted: int = 0 
    done = False

    for x in range(len(wasteland)):
        item: int = wasteland[x]
        while item > 0:
            item -= 1
            if reverse:   
                landmarks[(len(landmarks) - 1) - index] = least + x
            else:
                landmarks[index] = least + x
            num_sorted += 1
            if num_sorted == len(landmarks):
                done = True
            index += 1
        if done:
            break
    



#######Helper Functions#######
def find_extremes(landmarks: list) -> Union[int, int]:
    """ Helper function to find the maximum and minimum elements in a list in O(n) time

    Parameters
    ----------
    landmarks: List[int]
        List of integers to be searched
    

    Returns
    -------
    Two integers: the minimum value and the maximum value in that order
    """
    if landmarks == []:
        raise ValueError("Could not find maxima of the list")

    most, least = None, None

    for val in landmarks:
        if most == None or val > most:
            most = val
        if least == None or val < least:
            least = val
    return least, most
