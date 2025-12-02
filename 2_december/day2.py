with open("2_december/december2_input.txt") as file:
    lines = [line.strip() for line in file.readlines()]

print(f"Lines: {lines}")

beginning = []
end = []
invalidIDs = []

def loadranges():
    for line in lines:
        tokens = [t.strip() for t in line.split(',') if t.strip()]
        for token in tokens:
            
            a, b = token.split('-', 1)
            try:
                beginning.append(int(a))
                end.append(int(b))
            except ValueError:
                a_clean = ''.join(ch for ch in a if ch.isdigit())
                b_clean = ''.join(ch for ch in b if ch.isdigit())
                if a_clean and b_clean:
                    beginning.append(int(a_clean))
                    end.append(int(b_clean))
                else:
                    print(f"Skipping malformed token: {token}")

def printbeginningend():
    for i in range(len(beginning)):
        print(f"range: {beginning[i]} - {end[i]}")
        print()

def hasrepeatingdigits(value):
    strvalue = str(value)

    if len(strvalue) % 2 != 0:
        return False

    half = len(strvalue) // 2
    for i in range(half):
        if strvalue[i] != strvalue[i + half]:
            return False
        
    invalidIDs.append(value)
    print(f"Invalid ID found: {value}")

    return True

def solve():
    for i in range(len(beginning)):
        while beginning[i] <= end[i]:
            hasrepeatingdigits(beginning[i])
            beginning[i] += 1

def removeDuplicates(list):
    seen = set()
    result = []
    for item in list:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

def addAllItemsInCollection(collection):
    total = 0
    for item in collection:
        total += item
    return total


loadranges()
printbeginningend()
solve()

cleaned_invalidIDs = removeDuplicates(invalidIDs)

print(invalidIDs)

print(f"Total invalid IDs: {len(invalidIDs)}")
print(f"Total unique invalid IDs: {len(cleaned_invalidIDs)}")

print(f"Sum of all invalid IDs: {addAllItemsInCollection(cleaned_invalidIDs)}")





        