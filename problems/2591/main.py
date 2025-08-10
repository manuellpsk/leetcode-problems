class Solution:
    def distMoney(self, money: int, children: int) -> int:
        if money < children:
            return -1
        sol = [1] * children
        money -= children
        last_full_i = 0
        while money > 0:
            max_take = min(money, 8 if money == 10 and last_full_i == children - 2 else 7)
            sol[last_full_i] += max_take
            last_full_i += 1
            money -= max_take
            if last_full_i == children:
                sol[last_full_i - 1] += money
                break
        return len(list(filter(lambda e: e == 8, sol)))
