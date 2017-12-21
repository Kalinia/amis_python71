elements = [int(i) for i in input().split()]
print(elements)

def groups(elements, i=0, z=0, k=0):
    if i < len(elements) - 1 and elements[i] == elements[i + 1]:
        k += 1

        return groups(elements, i + 1, z, k)
    else:
        return k, z

def quantity(elements, i, k):
    if i < len(elements):
        d = groups(elements, i, 0, 1)
        if k < d[0]:
            k = d[0]
        return quantity(elements, i + 1, k)
    else:
        return k
print(quantity(elements, 0, 0))
