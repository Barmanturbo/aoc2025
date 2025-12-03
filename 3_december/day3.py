

def findHighestJoltage(bank):
    digits = [int(d) for d in bank]
    
    # just bruteforce all combinations of two digits; the input file isn't that large
    max_result = 0
    for battery1 in range(len(digits)):
        for battery2 in range(battery1+1, len(digits)):
            result = digits[battery1] * 10 + digits[battery2]
            max_result = max(max_result, result)
    
    return max_result
    
    
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

    