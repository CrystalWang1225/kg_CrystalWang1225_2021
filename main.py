import sys

MAXIMUM = 500

def isOneToOne(string1, string2):
    l1 = len(string1)
    l2 = len(string2)

    if l1 != l2:
        return False
    #If the length of the two strings are not the same, it is not one to one

    visited = MAXIMUM * [False]
    #assuming the maximum length this program can take is 500, this is all the character visited in string 2
    map = [-1] * MAXIMUM
    #map stores the mapping of every character in string1 to string2,map is initialized as all -1s for the start

    for i in range(l2):
        #For the character in string1 if it is the frist time occuring
        if map[ord(string1[i])] == -1:
            #put the character of string into visited
            visited[ord(string2[i])] = True

            map[ord(string1[i])] = string2[i] # store mapping of the current characters
        #if the current character has appeared already, need to make sure if the previous mapping is mapped to the same character in string 2
        elif map[ord(string1[i])] != string2[i]:
            return False

    return True;

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Invalid argument, valid argument python3 main.py string1 string2 ");

    print(isOneToOne(sys.argv[1],sys.argv[2]))





