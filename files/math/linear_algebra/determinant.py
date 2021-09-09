#count transpose
def permutation_exist(array):
    return True

def permutation(sequence):
    str_sequence = str(sequence)
    list_sequence = str_sequence.split()
    while(permutation_exist(list_sequence)):
        for j in list_sequence:
            print(j)

dim_seq = 1234
permutation(dim_seq)