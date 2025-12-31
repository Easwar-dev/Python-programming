class Solution:
    # function to print a square pattern of stars
    def pattern1(self,n):
        # outer loop handle rows
        for row in range(n):
            # inner loop to handle columns for each row
            for col in range(n):
                # print a stars followed by a space
                print("*",end=" ")
            # after printing starts in a row, move to the next line
            print()

    def pattern2(self,n):
        for row in range(n):
            for col in range(0,row+1):
                print("*",end=" ")
            print()

    def pattern3(self,n):
        for row in range(1,n+1):
            for col in range(1,row+1):
                print(col,end=" ")
            print()

    def pattern4(self,n):
        for row in range(1,n+1):
            for col in range(1,row+1):
                print(row,end=" ")
            print()

    def pattern5(self,n):
        for row in range(n):
            for col in range(n-row):
                print("*",end=" ")
            print()

    def pattern6(self,n):
        for row in range(n):
            for col in range(n-row):
                print(col+1,end=" ")
            print()

    def pattern7(self,n):
        # outer loop for rows
        for i in range(n):
            # print leading spaces
            for j in range(n - i - 1):
                print(" ",end="")
            # print stars
            for j in range(2 * i + 1):
                print("*",end="")
            # print trailing spaces
            for j in range(n - i - 1):
                print(" ",end="")

            # move to next row
            print()

    def pattern8(self,n):
        for i in range(n):
            for j in range(i):
                print(" ",end="")
            for j in range(2 * n - (2 * i + 1)):
                print("*",end="")
            for j in range(i):
                print(" ",end="")
            print()

    def pattern9(self,n):
        for i in range(n):
            # print spaces before stars
            print(" " * (n - i - 1), end="")
            # print stars
            print("*" * (2 * i + 1), end="")
            # print spaces after stars
            print(" " * (n - i - 1))
        for i in range(n):
            # print spaces before stars
            print(" " * i,end="")
            # print stars
            print("*" * (2 * n - (2 * i + 1)), end="")
            # print spaces after start
            print(" " * i)

    def pattern10(self,n):
        for i in range(2 * n):

            end = i
            if i > n: end = 2 * n - i

            for j in range(end):
                print("*",end="")

            print()

    def pattern11(self,n):
        # loop over the number of rows
        for i in range(n):
            # loop over the number is even, start with 1
            if i % 2 == 0:
                start = 1
            else:
                start = 0

            # loop to print alternating 1's and 0's
            for j in range(i + 1):
                print(start,end=" ")
                # alternate between 1 and 0
                start = 1 - start
            print()


# driver code
sol = Solution()
n = 5
sol.pattern11(n)