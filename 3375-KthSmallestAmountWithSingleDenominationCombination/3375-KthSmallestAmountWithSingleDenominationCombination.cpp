// Last updated: 23/08/2026, 23:27:44
class Solution {

    public:
        long long gcd(long long a, long long b) {
            while (b) {
                long long temp = a % b;
                a = b;
                b = temp;
            }
            return a;
        }

        long long lcm(long long a, long long b, long long limit) {
            long long g = gcd(a, b);

            if (a / g > limit / b)
                return limit + 1;

            long long result = (a / g) * b;

            if (result > limit)
                return limit + 1;

            return result;
        }

        long long count(long long x, vector<int>& coins) {
            int n = coins.size();
            long long ans = 0;

            for (int mask = 1; mask < (1 << n); mask++) {

                long long common = 1;
                int bits = 0;
                bool tooLarge = false;

                for (int i = 0; i < n; i++) {
                    if (mask & (1 << i)) {
                        bits++;

                        common = lcm(common, coins[i], x);

                        if (common > x) {
                            tooLarge = true;
                            break;
                        }
                    }
                }

                if (tooLarge)
                    continue;

                long long amount = x / common;

                if (bits % 2 == 1)
                    ans += amount;
                else
                    ans -= amount;
            }

            return ans;
        }

        long long findKthSmallest(vector<int>& coins, int k) {

            long long left = 1;

            long long right =
                1LL * (*min_element(coins.begin(), coins.end())) * k;

            while (left < right) {

                long long mid = left + (right - left) / 2;

                if (count(mid, coins) >= k)
                    right = mid;
                else
                    left = mid + 1;
            }

            return left;
        }
    };
