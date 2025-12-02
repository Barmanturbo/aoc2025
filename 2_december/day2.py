from multiprocessing import Pool, cpu_count, Manager

with open("2_december/december2_input.txt") as file:
    lines = [line.strip() for line in file.readlines()]

print(f"Lines have been loaded: {len(lines)} lines")

beginning = []
end = []

def loadRanges():
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

def printBeginningAndEnd():
    for i in range(len(beginning)):
        print(f"range: {beginning[i]} - {end[i]}")
        print()

def findFactors(value):
    factors = []
    for i in range(1, value + 1):
        if value % i == 0:
            factors.append(i)

    if factors[0] == 1 and len(factors)>2:
        factors.pop(0)
        factors.pop(-1)

    return factors

def hasRepeatingDigits(value):
    strvalue = str(value)
    length = len(strvalue)

    for chunk_size in range(1, length):
        if length % chunk_size != 0:
            continue

        chunk = strvalue[:chunk_size]
        inv = length // chunk_size

        if inv == 1:  # skip trivial full-length matches
            continue

        if chunk * inv == strvalue:
            return value  # return invalid ID

    return None  # valid number



def chunkNumbers(start, end_val, chunks):
    nums = list(range(start, end_val + 1))
    size = len(nums) // chunks or 1
    for i in range(0, len(nums), size):
        yield nums[i:i+size]

def processChunk(chunk):
    results = []
    for n in chunk:
        res = hasRepeatingDigits(n)
        if res is not None:
            results.append(res)
    return results



def solve():
    cores = cpu_count()
    tasks = []
    for start, end_val in zip(beginning, end):
        for chunk in chunkNumbers(start, end_val, cores * 4):
            tasks.append(chunk)

    invalidIDs_local = []
    with Pool(cores) as pool:
        results = pool.map(processChunk, tasks)

    for sublist in results:
        invalidIDs_local.extend(sublist)

    return invalidIDs_local

if __name__ == "__main__":
    loadRanges()
    invalidIDs = solve()
    cleaned_invalidIDs = sorted(set(invalidIDs))

    print(f"Total invalid IDs: {len(invalidIDs)}")
    print(f"Total unique invalid IDs: {len(cleaned_invalidIDs)}")
    print(f"Sum of all invalid IDs: {sum(cleaned_invalidIDs)}")
