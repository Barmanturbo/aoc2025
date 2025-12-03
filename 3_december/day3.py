

def findHighestJoltage(bank):
    digits = [int(d) for d in bank]
    keep_count = 12
    remove_count = len(digits) - keep_count
    
    # Use monotonic stack: remove smaller digits when we see larger ones
    stack = []
    for d in digits:
        # Remove smaller digits from stack if we have removals left
        while stack and stack[-1] < d and remove_count > 0:
            stack.pop()
            remove_count -= 1
        stack.append(d)
    
    # If we still have removals left, remove from the end
    while remove_count > 0:
        stack.pop()
        remove_count -= 1
    
    return int(''.join(map(str, stack[:keep_count])))
    
    
if __name__ == "__main__":
    with open("3_december/december3_input.txt", "r") as f:
        lines = f.readlines()
        print(f"Lines have been loaded: {len(lines)} lines")

    totalOutput = 0

    for bank in lines:
        bank = bank.strip()
        result = findHighestJoltage(bank)
        print(f"Line: {bank} => Highest Joltage: {result}") 
        totalOutput += result
    
    print(f"Total Output: {totalOutput}")

    