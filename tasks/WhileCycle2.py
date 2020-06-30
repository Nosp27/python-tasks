import random
from datetime import datetime, timedelta


class WhileCycleTask2:
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
