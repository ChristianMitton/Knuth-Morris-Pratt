def kmp(string, pattern):
    prefixes = getPrefixes(pattern)
    
    i,j = 0,0

    while i < len(string) and j < len(pattern):
        print(string[i], pattern[j])
        if string[i] != pattern[j]:       
            # while ptr[i] != ptrn[j] and i > 0, keep reseting i
            while string[i] != pattern[j] and j > 0:
                j = prefixes[j-1] if j > 0 else 0 # go back to previously stored idx         
            # j = prefixes[j-1] if j > 0 else 0
        if string[i] == pattern[j]:
            j += 1

        i += 1        

    return True if j >= len(pattern) else False    


def getPrefixes(pattern):
    #! each idx stores the length of a potential prefix ending at that pattern letter
    prefixes = [0 for _ in range(len(pattern))]
    i, j = 0, 1
    while j < len(pattern):
        # print(i,j)
        if pattern[j] == pattern[i]:
            prefixes[j] = i + 1
            i += 1            
            j += 1
        else:
            # while ptr[i] != ptrn[j] and i > 0, keep reseting i
            while pattern[i] != pattern[j] and i > 0:
                i = prefixes[i-1] if i > 0 else 0 # go back to previously stored idx         
            # check i and j again
            if pattern[j] == pattern[i]:
                lengthOfPrefix = i + 1
                prefixes[j] = lengthOfPrefix
                i += 1            
                j += 1
            else:
                j += 1     
    print(prefixes)    
    return prefixes


string = 'abcxabcdabxabcdabcdabcy'
string2 = 'abxabcabcaby'

p1 = 'abcdabcy'
p2 = 'abcaby'
p3 = 'aabaabaaa'

print(kmp(string2, p2))

           

# abcbcglx
# bcgl