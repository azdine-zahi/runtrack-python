L = ["Hello", "Morning", "Goodbye", "Takec-care"]
for a,b in [(0,3)]:
    L[a],L[b] = L[b],L[a]
    print(L)