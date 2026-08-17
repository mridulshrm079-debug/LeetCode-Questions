class Solution:
    def stoneGameV(self, a):
        n = len(a)

        # Prefix sums
        p = [0] * (n + 1)
        for i in range(n):
            p[i + 1] = p[i] + a[i]

        dp = [[0] * n for _ in range(n)]

        # left[l][r] =
        # max(dp[l][k] + prefix[k+1]) for l <= k <= r
        left = [[float('-inf')] * n for _ in range(n)]

        # right[l][r] =
        # max(dp[k][r] - prefix[k]) for l <= k <= r
        right = [[float('-inf')] * n for _ in range(n)]

        for i in range(n):
            left[i][i] = p[i + 1]
            right[i][i] = -p[i]

        for length in range(2, n + 1):

            for l in range(n - length + 1):
                r = l + length - 1

                total = p[r + 1] - p[l]

                # Find first split where left_sum >= right_sum
                lo, hi = l, r - 1
                k = r

                while lo <= hi:
                    mid = (lo + hi) // 2
                    left_sum = p[mid + 1] - p[l]

                    if 2 * left_sum >= total:
                        k = mid
                        hi = mid - 1
                    else:
                        lo = mid + 1

                best = 0

                # left_sum < right_sum
                if k > l:
                    best = max(
                        best,
                        left[l][k - 1] - p[l]
                    )

                # left_sum > right_sum
                if k < r:
                    best = max(
                        best,
                        right[k + 1][r] + p[r + 1]
                    )

                # Equal case
                if k < r and \
                   2 * (p[k + 1] - p[l]) == total:

                    s = p[k + 1] - p[l]

                    best = max(
                        best,
                        s + dp[l][k],
                        s + dp[k + 1][r]
                    )

                dp[l][r] = best

                # Update helper tables
                left[l][r] = max(
                    left[l][r - 1],
                    dp[l][r] + p[r + 1]
                )

                right[l][r] = max(
                    right[l + 1][r],
                    dp[l][r] - p[l]
                )

        return dp[0][n - 1]