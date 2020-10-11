import random


class BaseStrategy:
    def __init__(self, envelopes):
        self.envelopes = envelopes

    def __getitem__(self, item):
        return self.envelopes[item].value

    def play(self):
        """
        The base strategy- Locate an envelope by "feeling" for each and every envelope.
        :return: None
        """
        for envelope in self.envelopes:
            if random.randint(0, len(self.envelopes) - 1) == 0:
                print(f"I have a strong feeling about this one- ({envelope.value}$)")
                return
        print(f"Did not have a good feeling for any of them so we use last one- ({self[len(self.envelopes) - 1]}$)")

    def display(self):
        return "Finds by feeling"


class Automatic_BaseStrategy(BaseStrategy):
    def __init__(self, envelopes):
        super().__init__(envelopes)

    def play(self):
        """
        The Automatic Base Strategy- lottery of a random number.
        :return: None
        """
        print(f"Rolled out this envelope: ({self[random.randint(0, len(self.envelopes) - 1)]}$)")

    def display(self):
        return "Finds by random"


class N_max_strategy(BaseStrategy):
    def __init__(self, envelopes):
        super().__init__(envelopes)
        self.N = 0

    def play(self):
        """
        The N Max Strategy- Roll out a new maximum value N times.
        :return: None
        """
        index = 0
        max_values_counter = 1
        current_max_value = self[index]

        # loop and find N new maximum values. Save the value of the last envelope if reached the end.
        while max_values_counter < self.N:
            index += 1
            if self[index] > current_max_value:
                current_max_value = self[index]
                max_values_counter += 1
            if index == len(self.envelopes) - 1:
                current_max_value = self[len(self.envelopes) - 1]
                break
        print(f"The N max envelope is- {current_max_value}$")

    def display(self):
        return "Finds by the N max value"


class More_then_N_percent_group_strategy(BaseStrategy):
    def __init__(self, envelopes, percent):
        super().__init__(envelopes)
        self.percent = float(percent) * 100

    def play(self):
        """
        The More Then N Percent Group Strategy- Pass through a certain amount of envelopes and find the largest
        after that amount.
        :return: None
        """
        max_value = -1
        self.percent = int(float(self.percent) * 100)

        # Find the largest envelope for a percent of the envelopes.
        for i in range(self.percent):
            if self[i] > max_value:
                max_value = self[i]

        # Find the next largest envelope after.
        for i in range(self.percent, len(self.envelopes) + 1):
            if self[i] > max_value:
                print(f'Biggest envelope after {self.percent} envelopes- ({self[i]}$)')
                return  # break after finding a new one to deal with finishing through without finding.

        print(f"Did not find a larger envelope after N envelopes, so got last one- ({self[len(self.envelopes) - 1]}$)")

    def display(self):
        return "Find by more then N percent group strategy"
