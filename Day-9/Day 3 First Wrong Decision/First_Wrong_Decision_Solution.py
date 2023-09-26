def findFirstWrongDecision(decisions):
    for i, decision in enumerate(decisions):
        if decision == 'W':
            return i
    return -1

decisions = input().strip()

result = findFirstWrongDecision(decisions)
print(result)
