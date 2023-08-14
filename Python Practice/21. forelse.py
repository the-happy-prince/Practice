# Use else with for loops

for i in range(5):
    if i == 2:
        print("Else will run, because i could not reach its range, thus loop has been broken.")
        # break
    if i == 6:
        print("Else will not run, because i could reach its range.")
else:
    print("Else")

# Note: You can comment/uncomment break to test this code