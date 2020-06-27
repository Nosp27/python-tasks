from tasks import Task
import random


class WhileCycleTask:
    def description(self):
        return """
        Дан список из целых чисел. Найди в нем индекс, такой что сумма всех чисел слева, 
        включая число с индексом будет 
        максимально близка по значению к сумме чисел справа, не включая индекс.
        Например: x = [1,2,3,4,5] -> 2
         Потому что x[0] + x[1] + x[2] и x[3] + x[4] максимально близкие по значению.
        """

    def test_data(self):
        return [random.randint(0, 100) for _ in range(random.randint(5, 100))]

    def _solution(self, a):
        sums_diffs = []
        for i in range(len(a)):
            sums_diffs.append(abs(sum(a[:i]) - sum(a[i:])))

        min_sum = min(sums_diffs)
        for i in range(len(sums_diffs)):
            if sums_diffs[i] == min_sum:
                return max(i - 1, 0)

    def test(self, solution):
        tests = [self.test_data() for _ in range(10)]
        for test_case in tests:
            if self._solution(test_case) != solution(test_case):
                return False
        return True
