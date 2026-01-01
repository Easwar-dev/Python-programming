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

    def pattern12(self,n):
        # initial number of spaces in the first row
        spaces = 2 * (n - 1)
        # outer loop for the number of rows
        for i in range(1,n+1):
            # inner loop to print numbers in increasing order
            for j in range(1, i+1):
                print(j, end="")
            # inner loop to print spaces in the middle
            for j in range(1, spaces + 1):
                print(" ", end="")
            # inner loop to print numbers in decreasing order
            for j in range(i, 0, -1):
                print(j, end="")

            print()
            # decrease spaces by 2 after each row
            spaces -= 2

    def pattern13(self,n):
        num = 1
        for i in range(1, n+1):
            for j in range(1,i+1):
                print(num, end=" ")
                num += 1
            print()

    def pattern14(self,n):
        # outer loop for the number rows
        for i in range(n):
            # inner loop to print alphabets from A to A + i
            for j in range(i + 1):
                print(chr(65 + j), end=" ") # print the alphabet character followed by space
            print()

    def pattern15(self,n):
        for i in range(n):
            for j in range(0,n-i):
                print(chr(65 + j),end=" ")
            print()

    def pattern16(self,n):
        for i in range(n):
            for j in range(i+1):
                print(chr(65 + i), end=" ")
            print()

    def pattern17(self,n):
        for i in range(n):
            print(" " * (n - i - 1), end="")
            ch = ord('A')
            breakpoint = (2 * i + 1) // 2

            for j in range(1, 2 * i + 2):
                print(chr(ch), end="")
                if j <= breakpoint:
                    ch += 1
                else:
                    ch -= 1

            print()

    def pattern18(self,n):
        for i in range(n):
            # Print characters from ('A' + N - 1 - i) to ('A' + N - 1)
            for ch in range(ord('A') + n - 1 - i, ord('A') + n ):
                print(chr(ch), end=" ")

            print()

    def pattern19(self,n):
        # initial spaces for upper half
        inis = 0
        # loop for upper half rows
        for i in range(n):
            # Print stars on left
            print("*" * (n - i), end="")
            # Print spaces in middle
            print(" " * inis, end="")
            # Print stars on right
            print("*" * (n - i))
            # Increase middle spaces by 2
            inis += 2
        # Initial spaces for lower half
        inis = 2 * n - 2
        # Loop for lower half rows
        for i in range(1, n + 1):
            # print stars on left
            print("*" * i, end="")
            # print spaces in middle
            print(" " * inis, end="")
            # print stars on right
            print("*" * i)
            # Decrease middle spaces by 2
            inis -= 2

    def pattern20(self,n):
        spaces = 2 * n - 2
        for i in range(1, 2 * n):
            stars = i
            if i > n:
                stars = 2 * n - i
            print("*" * stars, end="")
            print(" " * spaces, end="")
            print("*" * stars)

            if i < n:
                spaces -= 2
            else:
                spaces += 2

    def pattern21(self,n):
        for i in range(n):
            for j in range(n):
                if i == 0 or j == 0 or i == n - 1 or j == n - 1:
                    print("*",end="")
                else:
                    print(" ",end="")
            print()

    def pattern22(self,n):
        for i in range(2 * n - 1):
            # Inner loop for columns
            for j in range(2 * n - 1):
                # Calculate distance from top
                top = i
                # Calculate distance from left
                left = j
                # Calculate distance from bottom
                bottom = (2 * n - 2) - i
                # Calculate distance from right
                right = (2 * n - 2) - j

                # Take the minimum of all four distances
                minDist = min(top, bottom, left, right)

                # Print number (starts with n at border, decreases inside)
                print(n - minDist, end=" ")
            # Move to the next row
            print()


# driver code
sol = Solution()
n = 5
sol.pattern22(n)