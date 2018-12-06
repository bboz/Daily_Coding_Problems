#Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
#For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

#givens
numbers=[10, 15, 3, 7]
k=17

def is_sum_available_in_list():
    for i in range(len(numbers)):
        numbers2=list(map(numbers[i] .__add__, numbers))
        if (k in numbers2 and i!=numbers2.index(k)):
            return 'True'," Index Of --> ",[i,numbers2.index(k)]
    return 'False'

is_sum_available_in_list()





