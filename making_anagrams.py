def number_needed(a, b):
    hash_a = {}
    hash_b = {}
    num_needed = 0
    for x in a:
        if x in hash_a:
            hash_a[x] = hash_a[x] + 1
        else:
            hash_a[x] = 1
    for x in b:
        if x in hash_b:
            hash_b[x] = hash_b[x] + 1
        else:
            hash_b[x] = 1
    for key, value in hash_a.iteritems():
        if key in hash_b:
            num_needed = num_needed + abs(hash_b[key] - hash_a[key])
        else:
            num_needed = num_needed + hash_a[key]
    for key, value in hash_b.iteritems():
        if key not in hash_a:
            num_needed = num_needed + hash_b[key]
        
    return num_needed

a = raw_input().strip()
b = raw_input().strip()

print number_needed(a, b)
