# Author: ARTEMIS
# Author 2: 
# Author 3: CREATE PR
# Author 4: NEW BRANCH WITH OPEN PR
# Author 5: branch again
def sort_numbers(numbers):
      n = len(numbers)
      for i in range(n):
          for j in range(0, n - i - 1):
              if numbers[j] > numbers[j + 1]:
                  numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
      return numbers