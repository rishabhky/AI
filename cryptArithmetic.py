from itertools import permutations
    
def is_valid_solution(word1,word2,result,mapping):
    def word_to_number(word):
        return sum(mapping[letter]*(10**i)for i,letter in enumerate(reversed(word)))
    
    num1=word_to_number(word1)
    num2=word_to_number(word2)
    num_result=word_to_number(result)

    return num1+num2==num_result

def solve_cryptarithmetic(word1,word2,result):
    unique_letters=set(word1+word2+result)  

    if len(unique_letters)>10:
        print("Error:Too many unique letters")
        return
    
    letters=list(unique_letters)
    digits=range(10)

    for perm in permutations(digits,len(letters)):

        mapping=dict(zip(letters,perm))

        if mapping[word1[0]]==0 or mapping[word2[0]]==0 or mapping[result[0]]==0:
            continue

        if is_valid_solution(word1,word2,result,mapping):
            print(f"Solution found: {mapping}")
            return mapping

    print("No solution found") 


solve_cryptarithmetic("SEND","MORE","MONEY")