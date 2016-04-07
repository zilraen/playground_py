################################################################################
#   Some consecutive pages had been teared up from the book.
#   The sum of numbers on these pages is neededSum.
#   What pages had been teared up?
#
# X + X + 1             = 2X + 1       # numbers on Xth page
# X + 1 + X + 1 + 1     = 2X + 3       # numbers on (X + 1)th page
# X + 2 + X + 2 + 1     = 2X + 5       # numbers on (X + 2)th page
# X + 3 + X + 3 + 1     = 2X + 7       # numbers on (X + 3)th page
# X + 4 + X + 4 + 1     = 2X + 9       # numbers on (X + 4)th page
# ...
# X + N + X + N + 1     = 2X + 2N + 1  # numbers on (X + N)th page
#
# 2X + 1                               # 1
# 2X + 1 + 2X + 3       = 4X + 4       # 1 + 2
# (4X + 4) + 2X + 5     = 6X + 9       # 1 + 2 + 3
# (6X + 9) + 2X + 7     = 8X + 16      # 1 + 2 + 3 + 4
# (8X + 16) + 2X + 9    = 10X + 25     # 1 + 2 + 3 + 4 + 5
# 2NX + NN                             # 1 + 2 + 3 +...+ N
#
# 2NX + NN = neededSum
# 2NX = neededSum - NN
# X = (neededSum - NN) / (2N)
################################################################################

neededSum = 112
accuracy = neededSum / 10
pagesStartsFromEven = 0
stopOnFirstMatch = False
solutions = []

print "Needed pages sum is", neededSum, ", page numbers starts from", ("even." if pagesStartsFromEven else "odd.")
print "Approximate results:"
for N in range(1, neededSum / 2):
    x = int(float(neededSum - N*N) / (2*N))
    if (x % 2 == pagesStartsFromEven):
        x = x - 1

    if x > 0:
        pages = []
        sum = 0
        for i in range(x, x + 2*N):
            pages.append(i)
            sum += i
        if abs(sum - neededSum) < accuracy:
            print N, "pages, starting from", x, ":"
            print "    ", pages, " = ", sum, ("        <== EXACT MATCH!" if sum == neededSum else "")

            if sum == neededSum:
                solutions.append(pages)
                if stopOnFirstMatch:
                    break

print "__________________"
if len(solutions) == 1:
    print "Solution is:", solutions[0]
elif len(solutions) > 1:
    print "Solutions are:", solutions
else:
    print "NO SOLUTION FOUND"
