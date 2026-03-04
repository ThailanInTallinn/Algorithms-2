
def miss_alpha(target:str):
    seen = [0 for _ in range(0, 26)]

    for i in range(0, len(target)):
        if(target[i] in [',', '.', ' ']):
            continue
        elif(target[i].isupper()):
            continue

        seen[ord(target[i]) - 97] = 1

    return [chr(i + 97) for i in range(0, len(seen)) if seen[i] == 0]


string_alvo = "I am the way, and the truth, and the life. No one comes to the Father except through me" 

result = miss_alpha(string_alvo)
print(result)
