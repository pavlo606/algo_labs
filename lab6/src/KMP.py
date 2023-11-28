def prefix(string: str):
    i = 1
    j = 0
    p = [0] * len(string)
    while i < len(string):
        if string[i] == string[j]:
            p[i] = j + 1
            i += 1
            j += 1
        elif j == 0:
            p[i] = 0
            i += 1
        else:
            j = p[j - 1]
    return p


def KMP(string, substring):
    if not substring:
        return [i for i in range(len(string))]
    p = prefix(substring)

    k = 0
    l = 0
    sub_indexes = []

    while k < len(string):
        if string[k] == substring[l]:
            k += 1
            l += 1
            if l == len(substring):
                sub_indexes.append(k - len(substring))
                l = p[l - 1]

        elif l == 0:
            k += 1

        else:
            l = p[l - 1]

    return sub_indexes


string = "abababacdabababa"
sub_string = "ababa"

print(KMP(string, sub_string))
