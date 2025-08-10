from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        i, buy = self.get_min(prices)
        j, sell = self.get_max(prices)
        if i < j:
            return sell - buy
        else:
            i = 0
        len_p = len(prices)
        while i < len_p - 1:
            buy = prices[i]
            if j < i+1:
                j, sell = self.get_max(prices, i+1)
            profit = sell - buy
            if profit > max_profit:
                max_profit = profit
            i += 1
        if max_profit < 0:
            max_profit = 0
        return max_profit

    def get_max(self, prices: List[int], start: int = 0):
        len_prices = len(prices)
        i = start
        max_value = prices[i]
        max_i = start
        i += 1
        while i < len_prices:
            if prices[i] > max_value:
                max_value = prices[i]
                max_i = i
            i += 1
        return max_i, max_value

    def get_min(self, prices: List[int], start: int = 0):
        len_prices = len(prices)
        i = start
        min_value = prices[i]
        min_i = start
        i += 1
        while i < len_prices:
            if prices[i] < min_value:
                min_value = prices[i]
                min_i = i
            i += 1
        return min_i, min_value
