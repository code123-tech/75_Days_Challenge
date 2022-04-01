from collections import defaultdict


class Solution:
    def invalidTransactions(self, transactions):
        if not transactions:
            return []
        dicti = defaultdict(list)

        for t in transactions:
            name, time, money, city = t.split(",")
            time = int(time)
            money = int(money)
            dicti[name].append([time, city])
        ans = []
        for t in transactions:
            name, time, money, city = t.split(",")
            time, money = int(time), int(money)
            if money > 1000:
                ans.append(t)
            else:
                prev_trans = dicti[name]
                for prev_time, prev_city in prev_trans:
                    if abs(time-prev_time) <= 60 and prev_city != city:
                        ans.append(t)
                        break
        return ans


sol = Solution()
sol.invalidTransactions(
    ["alice,20,800,mtv", "alice,50,100,mtv", "alice,51,100,frankfurt"])
