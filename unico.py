def unico(target:str):
    seen = [0 for i in range(0, 26)]
    
    for i in range(0, len(target)):
        seen[ord(target[i]) - 97] += 1

    for i in range(0, len(seen)):
        if seen[i] == 1:
            return (chr(i + 97), seen)

target_str = "civic"
result:tuple[str, list[int]] = unico(target_str)

print(f"Primeiro caractere não repetido em {target_str} : {result[0]}")
print(f"Contagem de frequência dos caracters em {target_str}('a' -> index 0, etc) \n{result[1]}")
