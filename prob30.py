"""
    For a given list of sequential integers, return True if any 3 members form an arithmetic sequence
"""
def has_sequence(numbers):
    if len(numbers) < 3: return False 

    i_sl = numbers[0:len(numbers)-2]
    #print("..i range:", i_sl)
    for i in enumerate(i_sl):
        j_sl = numbers[i[0]+1:len(numbers)-1]
        #print("..j range:", j_sl)
        for j in enumerate(j_sl, i[0]+1):
            k_sl = numbers[j[0]+1:len(numbers)]
            #print("..k range:", k_sl)
            for k in enumerate(k_sl, j[0]+1):
                #print("....check:", i[1], j[1], k[1])
                if j[1] - i[1] == k[1] - j[1]: return True 

    return False

"""
    Find the n+1th integer from a passed in set of n
    Will incrementally check from the specified start point and up to 20
    returns the first match or 0 no valid options found
"""
def find_next(existing, start):
    # Extend list to hold the candidate integer
    mapped = existing.copy()
    mapped.append(0)
    for i in list(range(start,21)):
        mapped[len(mapped)-1] = i
        if not has_sequence(mapped):
            return i
    return 0

def solve_nested():
    for i1 in range(1, 13):
        for i2 in range(i1+1, 14):
            target = [i1, i2]
            i3 = find_next(target, i2 + 1)
            target.append(i3)
            while i3 != 0 and i3 < 15:
                i4 = find_next(target, i3 + 1)
                target.append(i4)
                while i4 != 0 and i4 < 16:
                    i5 = find_next(target, i4 + 1)
                    target.append(i5)
                    while i5 != 0 and i5 < 17:
                        i6 = find_next(target, i5 + 1)
                        target.append(i6)
                        while i6 != 0 and i6 < 18:
                            i7 = find_next(target, i6 + 1)
                            target.append(i7)
                            while i7 != 0 and i7 < 19:
                                i8 = find_next(target, i7 + 1)
                                target.append(i8)
                                while i8 != 0 and i8 < 20:

                                    i9 = find_next(target, i8 + 1)
                                    if i9 == 0:
                                        i8 = find_next(target, i8 + 1)
                                    else:
                                        target.append(i9)
                                        return target
                                # end inner
                                del target[7]                                            
                                i7 = find_next(target, i7+1)           
                            # end inner
                            del target[6]                                            
                            i6 = find_next(target, i6+1)           
                        # end inner
                        del target[5]                                            
                        i5 = find_next(target, i5+1)           
                    # end inner
                    del target[4]        
                    i4 = find_next(target, i4+1)
                # end inner
                del target[3]
                i3 = find_next(target, i3+1)
                target[2] = i3
            # end inner
            del target[2]

    return 0

def run():
    return solve_nested()         


