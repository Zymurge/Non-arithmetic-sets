def has_sequence(numbers, end):
    """ For a given list of sequential integers, return True if any 3 members form an arithmetic sequence.
        Assess the list from the start through to the specified end, ignoring members beyond that limit.
        Will short circuit and return False if there are less than 3 non-zero numbers to begin the sequence.
    """
    if end < 3 | len(numbers) < end:
        return False 

    # Need the search sets to be inclusive of the end
    end += 1

    i_sl = numbers[0:end-2]
    #print("..i range:", i_sl)
    for i in enumerate(i_sl):
        j_sl = numbers[i[0]+1:end-1]
        #print("..j range:", j_sl)
        for j in enumerate(j_sl, i[0]+1):
            k_sl = numbers[j[0]+1:end]
            #print("..k range:", k_sl)
            for k in enumerate(k_sl, j[0]+1):
                #print("....check:", i[1], j[1], k[1])
                if j[1] - i[1] == k[1] - j[1]: return True 

    return False

def find_next(existing, pos):
    """ Finds the next valid integer that fits the sequence.
        Starts at position 'pos' from the passed in set and find the next fitting integer under 21.
        Assumes lowest value initial value is 0 and will not exceed 20. Updates 'existing' with the 
        value found and returns that value, or 0 if no valid options found.
    """
    # For a beginning value, start with the previous positions value, since numbers must be sequentials
    if existing[pos] < existing[pos - 1]:
        existing[pos] = existing[pos - 1]

    for i in range(existing[pos]+1,21):
        existing[pos] = i
        if not has_sequence(existing, pos):
            return i
    existing[pos] = 0
    return 0

def find_next_recursive(target):
    """ Finds the first solution by iterating from the first position containing a 0.
        Recursively called for each subsequent position out to the 9th.
        Returns a valid array of integers or 0 if none found.
    """
    # determine position of first zero value
    pos = 0
    for i,v in enumerate(target):
        if v == 0:
            pos = i
            break
    
    # loop through each valid value
    find_next(target, pos)
    # if 9th (zero based) position return solution
    if target[8] != 0:
        return target
        
    while target[pos] > 0:
        # recurse until 9th position is filled
        if find_next_recursive(target) == 0:
            find_next(target, pos)
        else:
            return target

    # fall through fail
    return 0

def run():
    target = [0] * 9
    return find_next_recursive(target) 


