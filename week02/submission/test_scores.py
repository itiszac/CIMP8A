#! /usr/bin/env python3

# Display welcome message
print("The Test Scores Program\n")
print("Enter Test scores\nEnter \'Exit\' to Quit")
print("=" * 25)

# Get scores from user
total = 0
count = 0
test_score = 0
while test_score != "exit":
  test_score = input("Enter test score: ")

  if test_score.lower() == "exit":
    break

  count += 1
  total += int(test_score)

# Calculate average
average_score = round(total / count)

# Format and display results
print("=" * 25)
print("# of Score: ", str(count),
      "\nTotal Score:  ", str(total),
      "\nAverage Score: ", str(average_score))

# End application
print("\nBye")
