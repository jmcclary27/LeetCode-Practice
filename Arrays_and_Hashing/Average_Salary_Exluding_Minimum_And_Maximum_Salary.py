class Solution:
    def average(self, salary: list[int]) -> float:
        if salary[0] > salary[1]:
            maxx = salary[0]
            minn = salary[1]
        else:
            maxx = salary[1]
            minn = salary[0]
        total = 0
        for i in range(2, len(salary)):
            sal = salary[i]
            if sal > maxx:
                total += maxx
                maxx = sal
                print(f'maxx choice: {sal}')
            elif sal < minn:
                total += minn
                minn = sal
                print(f'minn choice: {sal}')
            else:
                total += sal
                print(f'else choice: {sal}')
        return total / (len(salary) - 2)