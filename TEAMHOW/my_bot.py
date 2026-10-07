# Team Name: TEAMHOW
# Members: Nayan Das , Ayan Sahana , Sabuj Bhunia
# Mentor: Akshat

import math


class Bot:

    def move(self, obs):
        # Version 1: don't use PEEK or SWAP yet
        return None

    def fair_value(self, obs):
        # Cards whose values we directly know
        known_sum = sum(obs["hand"]) + sum(obs["board"])
        known_sum += sum(obs["opp_known"])

        # unseen[r-1] = number of unseen cards of rank r
        unseen = obs["unseen"]

        total_unseen = sum(unseen)

        if total_unseen == 0:
            return known_sum

        # Expected value of one unseen card
        unseen_sum = sum(
            (rank + 1) * count
            for rank, count in enumerate(unseen)
        )

        average_unseen = unseen_sum / total_unseen

        return known_sum + total_unseen * average_unseen

    def quote(self, obs):
        value = self.fair_value(obs)

        # Round to a sensible price
        return round(value, 2)

    def respond(self, obs, price):
        fair = self.fair_value(obs)

        position = obs["position"]

        # Actual execution prices:
        buy_price = price + 2
        sell_price = price - 2

        # How much advantage do we have?
        buy_edge = fair - buy_price
        sell_edge = sell_price - fair

        # Buy if meaningfully cheap
        if buy_edge > 1.0:
            room = 10 - position
            return min(2, room)

        # Sell if meaningfully expensive
        if sell_edge > 1.0:
            room = 10 + position
            return -min(2, room)

        return 0