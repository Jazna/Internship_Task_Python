def print_hex_pattern(rows, cols):
    for row in range(rows):
        # Print the top part of the hexagons
        if row % 2 == 0:
            for col in range(cols):
                print(" __ ", end=" ")
            print()
        
        # Print the middle part of the hexagons
        for col in range(cols):
            if col == 0:
                print("/", end="")
            else:
                print(" /", end="")
            print("  \\", end="")
        print()
        
        # Print the bottom part of the hexagons
        for col in range(cols):
            if col == 0:
                print("\\__", end="")
            else:
                print("/ \\", end="")
        print("/")

# Input dimensions
print("inputs :- 4 7")
print_hex_pattern(4, 7)
print()
print("inputs :- 3 5")
print_hex_pattern(3, 5)
print()
