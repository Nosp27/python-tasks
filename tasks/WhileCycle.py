import random
from datetime import datetime, timedelta


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


class NastyaDoingPython:
    def description(self):
        return """
        Настя Лелушка планирует свой день. В N утра она решает позавтракать овсяночкой
        и сесть за питон и делать его до M часов (тип datetime).

        Но на самом деле оказывается что после S минут задача слишком сложная, Настя зовет на помощь Пашу.
        После этого Настя снова садится за питон только через X минут. Каждую минуту, когда Настя сидит за питоном, она 
        решает 0.04 задачки.

        Сколько Настя просидит за питоном?
        Сколько задач Настя решит за день?

        (N, M, S, X) даны (tuple из (datetime, datetime, timedelta, timedelta)).
        """

    def test_data(self):
        now = datetime.now()
        return (
            datetime(
                year=now.year, month=now.month, day=now.day, hour=random.randint(9, 10), minute=random.randint(0, 59)
            ),
            datetime(
                year=now.year, month=now.month, day=now.day, hour=random.randint(13, 18), minute=random.randint(0, 59)
            ),
            timedelta(minutes=random.randint(5, 49)),
            timedelta(minutes=random.randint(6, 45)),
        )

    def _solution(self, a):
        N, M, S, X = a

        pythoned_time = timedelta(seconds=0)
        tasks = 0.0
        step = timedelta(minutes=1)

        current_time = N
        stop_time = M
        task_acc = timedelta(minutes=0)
        while current_time < stop_time:
            if task_acc == S:
                current_time += timedelta(minutes=40)
                task_acc = timedelta(minutes=0)
            if not current_time < stop_time:
                break
            pythoned_time += step
            current_time += step
            task_acc += step
            tasks += 0.04
        return pythoned_time, int(tasks)

    def test(self, solution):
        tests = [self.test_data() for _ in range(10)]
        for test_case in tests:
            if self._solution(test_case) != solution(test_case):
                return False
        return True


class SortListCycle:
    def description(self):
        return """
        Тебе дан список. Нужно его отсортировать по возрастанию
        """

    def test_data(self):
        return [random.randint(1, 10000) for _ in range(random.randint(0, 100))]

    def _solution(self, a):
        return sorted(a)

    def test(self, solution):
        tests = [self.test_data() for _ in range(10)]
        for test_case in tests:
            if self._solution(test_case) != solution(test_case):
                return False
        return True

