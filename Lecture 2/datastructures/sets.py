# Create an empty set
s = set()

# Add elements to set
s.add(1)
s.add(2)
s.add(3)
s.add(4)
s.add(3)  # Duplicate element, will not be added

s.remove(2) # Remove element 2 from the set
print(s)

print(f"This set has {len(s)} elements.")