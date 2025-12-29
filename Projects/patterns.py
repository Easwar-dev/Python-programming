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

# driver code
sol = Solution()
n = 5
sol.pattern6(n)