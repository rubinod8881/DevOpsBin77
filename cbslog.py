with open(r'C:\Windows\Logs\CBS\CBS.log', 'r', encoding='utf-8', errors='ignore') as f:
    for line in f:
        if "error" in line.lower():
            print(line)