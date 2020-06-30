import requests


class CountTask:
    def __init__(self):
        self.data = None

    def description(self):
        return """
        Посчитай в тексте слова.
        
        Собери из них словарик {слово: количество}
        
        Не забудь что для проверки в test() надо кинуть не сам ответ, 
        а функцию которая его находит
        
        def my_solution():
            ...
        
        test(my_solution)
        """

    def test_data(self):
        if not self.data:
            print("Downloading Data")
            self.data = requests.get("https://norvig.com/big.txt").text
            print("Data Collection Completed")
        return self.data

    def _solution(self, a):
        res = dict()
        for word in self.test_data().split(" "):
            if word in res:
                res[word] += 1
            else:
                res[word] = 1
        return res

    def test(self, solution):
        data_for_test = solution(self.test_data())
        print("Counted data for test")
        data_expected = self._solution(self.test_data())
        print("Counted data expected")
        return data_for_test == data_expected
