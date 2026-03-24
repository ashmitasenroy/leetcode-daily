class Solution:
    def constructProductMatrix(self, grid):
        MOD = 12345
        
        # flatten grid
        arr = []
        for row in grid:
            for val in row:
                arr.append(val % MOD)

        n = len(arr)

        # prefix
        prefix = [1] * n
        for i in range(1, n):
            prefix[i] = (prefix[i-1] * arr[i-1]) % MOD

        # suffix
        suffix = [1] * n
        for i in range(n-2, -1, -1):
            suffix[i] = (suffix[i+1] * arr[i+1]) % MOD

        # result
        res = [0] * n
        for i in range(n):
            res[i] = (prefix[i] * suffix[i]) % MOD

        # reshape back to grid
        idx = 0
        ans = []
        for row in grid:
            new_row = []
            for _ in row:
                new_row.append(res[idx])
                idx += 1
            ans.append(new_row)

        return ans