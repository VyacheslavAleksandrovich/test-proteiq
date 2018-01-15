from itertools import combinations_with_replacement, count, takewhile, izip


def sieve_erathosh_f(list_of_numbers):
    if len(list_of_numbers) == 0: return []
    else:
        return list_of_numbers[:1] + sieve_erathosh_f(filter(lambda x: x % list_of_numbers[0] != 0, list_of_numbers[1:]))
    
def get_all_prime_to_num(num):
    return sieve_erathosh_f(range(2,num))

def get_two_opts(num, primes):
    _prime = ((x,y,z) for x,y,z in combinations_with_replacement(primes, 3) if x+y+z == num)
    return [(x, y, z) for i, (x,y,z) in takewhile(lambda (x, y): x < 2, izip(count(), _prime))]
