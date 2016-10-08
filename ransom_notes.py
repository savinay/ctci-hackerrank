def ransom_note(magazine, ransom):
    map_ransom = {}
    flag = True
    for word in ransom:
        if word in map_ransom:
            map_ransom[word] = map_ransom[word] + 1
        else:
            map_ransom[word] = 1
    map_magazine = {}
    for word in magazine:
        if word in map_magazine:
            map_magazine[word] = map_magazine[word] + 1
        else:
            map_magazine[word] = 1
    print map_magazine
    print map_ransom
    for key, value in map_ransom.iteritems():
        if key in map_magazine:
            print value, map_magazine[key]
            if value > map_magazine[key]:
                flag = False
                return flag
        else:
            flag = False
            return flag
    return flag
    

m, n = map(int, raw_input().strip().split(' '))
magazine = raw_input().strip().split(' ')
ransom = raw_input().strip().split(' ')
answer = ransom_note(magazine, ransom)
if(answer):
    print "Yes"
else:
    print "No"