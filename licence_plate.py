def licenseKeyFormatting(s: str, k: int) -> str:
        items = list(s.upper())
        while "-" in items:
            items.remove("-")
        min_lenght = len(items)//k
        reminder = len(items)%k
        extra_index = 0
        if reminder == 0:
            for i in range(1,min_lenght):
                items.insert((extra_index + (i*k)), "-")
                extra_index += 1
        else:
            if(reminder < len(items)):
                items.insert((reminder), "-")
                extra_index += 1
            for i in range(1, min_lenght+1):
                if (extra_index + reminder + (i*k)) < len(items):
                    items.insert((extra_index + reminder + (i*k)), "-")
                    extra_index += 1
        string = ""
        string.join(items) 
        return string.join(items) 

print(licenseKeyFormatting("a0001afds-", 4))
print(licenseKeyFormatting("5F3Z-2e-9-w", 4))
print(licenseKeyFormatting("2-5g-3-J", 2))