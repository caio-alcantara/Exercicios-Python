num = int(input("De qual número você deseja a tabuada? "))
print(f"A tabuada do {num} é:")
for c in range(1, 11):
    print(f"{num} x {c} = {c * num}")
