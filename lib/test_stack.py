from Stack import Stack

# Create stack
stk = Stack(limit=5)
print("Stack created with limit 5")

# Test isEmpty
print("Is empty:", stk.isEmpty())

# Push items
stk.push(1)
stk.push(2)
stk.push(3)
print("Pushed 1,2,3")

# Test size
print("Size:", stk.size())

# Test peek
print("Peek:", stk.peek())

# Test search
print("Search 2:", stk.search(2))  # Should be 1 (from top: 3 at 0, 2 at 1)
print("Search 4:", stk.search(4))  # -1

# Pop
popped = stk.pop()
print("Popped:", popped)

# Test full
stk.push(4)
stk.push(5)
print("Full:", stk.full())

# Try push when full
try:
    stk.push(6)
except ValueError as e:
    print("Push on full:", e)

# Try pop on empty after popping all
stk.pop()
stk.pop()
stk.pop()
stk.pop()
print("Is empty after pops:", stk.isEmpty())

try:
    stk.pop()
except ValueError as e:
    print("Pop on empty:", e)

print("All tests passed!")
