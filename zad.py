#txt = [int(t) for t in input().split(', ')]
#print(*txt [::-1], sep =" | ")


# text = list(mp(int, input().split(', ')))
#print(*text [::-1])

#print(*input().split(', ')[::-1])

text = input().split(', ')
for i in range(len(text)):
    print(text.pop(), end=' ')