
def sum_by_fouth(n):
    if isinstance(n, int) and n >= 0:
        sum = 0
        for i in range(n):
            if i % 4 == 0:
                sum += i 
        return sum
    else:
        raise ValueError("Uncorrect value!")
    
print(sum_by_fouth(10))