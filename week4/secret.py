class Solution(object):
    def peopleAwareOfSecret(self, n, delay, forget):
        """
        :type n: int
        :type delay: int
        :type forget: int
        :rtype: int
        """
        MOD = 10**9 + 7
        dp = [0] * (n + 1)
        dp[1] = 1

        sharing = 0  # number of people eligible to share today

        for day in range(2, n + 1):
            # add those who start sharing today
            if day - delay >= 1:
                sharing = (sharing + dp[day - delay]) % MOD
            # remove those who forget today (they cannot share today)
            if day - forget >= 1:
                sharing = (sharing - dp[day - forget]) % MOD
            dp[day] = sharing  # these newly told people learned today

        # sum of people who haven't forgotten by end of day n
        start = max(1, n - forget + 1)
        return sum(dp[start:n + 1]) % MOD