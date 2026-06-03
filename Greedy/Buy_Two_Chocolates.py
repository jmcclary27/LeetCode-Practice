class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        minn, nextt = None, None

        for price in prices:
            if not minn or price <= minn:
                nextt = minn
                minn = price
            elif not nextt or price <= nextt:
                nextt = price
        
        total = nextt + minn
        return money - total if total <= money else money