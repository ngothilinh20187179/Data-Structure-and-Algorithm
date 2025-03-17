def group_anagrams(array_strings):
    dictionary = {}
    for string in array_strings:
        key = sort_string(string)
        if key in dictionary:
            dictionary[key].append(string)
        else:
            dictionary[key] = [string]
    dictionary_values = dictionary.values()
    return list(dictionary_values)

def sort_string(string):
    sort_char = sorted(string)
    sort_string = "".join(sort_char)
    return sort_string

print("1st set:")
print( group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) )

print("\n2nd set:")
print( group_anagrams(["abc", "cba", "bac", "foo", "bar"]) )

print("\n3rd set:")
print( group_anagrams(["listen", "silent", "triangle", "integral", "garden", "ranged"]) )



"""
    EXPECTED OUTPUT:
    ----------------
    1st set:
    [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]

    2nd set:
    [['abc', 'cba', 'bac'], ['foo'], ['bar']]

    3rd set:
    [['listen', 'silent'], ['triangle', 'integral'], ['garden', 'ranged']]

"""