def all_permutations(seq):
    #if it is empty list, return emtpy list
    if len(seq) == 0:
        return []

    #if we have only one element, return this element
    if len(seq) == 1:
        return [seq]

    #create empty list where we will store different permucations
    perm = []


    for i in range(len(seq)):
        #take one element from initial list, for the first iteration it will be first element
        m = seq[i]

        #create additional list without above mentioned element
        reminding_seq = seq[:i] + seq[i + 1:]

        #evoke again the same function (recursion) with newly created list
        for p in all_permutations(reminding_seq):
            #append to the list with permutation the element with what function has returned (recusive function)
            perm.append([m] + p)

    return perm

def possible_permutations(seq):
    #calling additional function where all permutations are stored in list
    permutations = all_permutations(seq)

    #generator which yield one perm at a time
    for a_perm in permutations:
        yield a_perm


[print(n) for n in possible_permutations([1, 2, 3])]
