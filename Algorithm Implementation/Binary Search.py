
def binary_search(arr, target):
    start = 0
    end = len(arr) - 1

    while start <= end:
        mid = (start + end) // 2
        print(f"Checking middle index {mid}, value {arr[mid]}")

        if arr[mid] == target:
            print(f"\n✅ Element {target} found at index {mid}")
            return mid
        elif arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1

    print(f"\n❌ Element {target} not found in the list.")
    return -1


# ---------- Main Program ----------
print("🔹 Binary Search Algorithm 🔹")
n = int(input("Enter number of elements: "))

# user input list
arr = []
for i in range(n):
    val = int(input(f"Enter element {i+1}: "))
    arr.append(val)

# list must be sorted
arr.sort()
print(f"\nSorted List: {arr}")

# element to search
target = int(input("Enter element to search: "))

# call function
binary_search(arr, target)

