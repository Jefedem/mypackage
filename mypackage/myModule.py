def top_n(items, n):
    """Return the top n items in an array, in desc order
    
    Args:
        items (array): list or array-like object
        n (int): num of items to return
        
    Return:
        array: top n items, in desc order
        
    Egs:
        >>> top_([8,3,2,7,4], 3)
        [8,7,3]
    """
    for i in range(n): # keep sorting until we have the top items
        for j in range(len(items)-1-i):
            
            if items[j] > items[j+i]: # if this item is bigger than next item..
                items[j], items[j+i] = items[j+1], items[j] # swap the two!
                
    # get last two items
    top_n = items[-n:]
    
    # return in descending order
    return top_n[::-1]