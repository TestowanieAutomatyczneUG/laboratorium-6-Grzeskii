import math


def statement(invoice, plays):
    total_amount = 0
    volume_credits = 0
    result = f'Statement for {invoice["customer"]}\n'

    def format_as_dollars(amount):
        return f"${amount:0,.2f}"

    for perf in invoice['performances']:
        play = plays[perf['playID']]
        if play['type'] == "tragedy":
            this_amount = 40000
            if perf['audience'] > 30:
                this_amount += 1000 * (perf['audience'] - 30)
        elif play['type'] == "comedy":
            this_amount = 30000
            if perf['audience'] > 20:
                this_amount += 10000 + 500 * (perf['audience'] - 20)

            this_amount += 300 * perf['audience']

        else:
            raise ValueError(f'unknown type: {play["type"]}')

        # add volume credits
        volume_credits += max(perf['audience'] - 30, 0)
        # add extra credit for every ten comedy attendees
        if "comedy" == play["type"]:
            volume_credits += math.floor(perf['audience'] / 5)
        # print line for this order
        result += f' {play["name"]}: {format_as_dollars(this_amount/100)} ({perf["audience"]} seats)\n'
        total_amount += this_amount

    result += f'Amount owed is {format_as_dollars(total_amount/100)}\n'
    result += f'You earned {volume_credits} credits\n'
    return result


import unittest

class testStatement(unittest.TestCase):

    def test_statement_for_tragedy_and_audience_lt_30(self):
        self.assertEqual(statement({"customer": "BigCo", "performances": [{"playID": "hamlet", "audience": 25}]}, {"hamlet": {"name": "Hamlet", "type": "tragedy"}}),
                         "Statement for BigCo\n Hamlet: $400.00 (25 seats)\nAmount owed is $400.00\nYou earned 0 credits\n")

    def test_statement_for_tragedy_and_audience_gt_30(self):
        self.assertEqual(statement({"customer": "BigCo", "performances": [{"playID": "hamlet", "audience": 32}]}, {"hamlet": {"name": "Hamlet", "type": "tragedy"}}),
                         "Statement for BigCo\n Hamlet: $420.00 (32 seats)\nAmount owed is $420.00\nYou earned 2 credits\n")

    def test_statement_for_comedy_and_audience_lt_20(self):
        self.assertEqual(statement({"customer": "BigCo", "performances": [{"playID": "hamlet", "audience": 15}]}, {"hamlet": {"name": "Hamlet", "type": "comedy"}}),
                         "Statement for BigCo\n Hamlet: $345.00 (15 seats)\nAmount owed is $345.00\nYou earned 3 credits\n")

    def test_statement_for_comedy_and_audience_gt_20(self):
        self.assertEqual(statement({"customer": "BigCo", "performances": [{"playID": "hamlet", "audience": 25}]}, {"hamlet": {"name": "Hamlet", "type": "comedy"}}),
                         "Statement for BigCo\n Hamlet: $500.00 (25 seats)\nAmount owed is $500.00\nYou earned 5 credits\n")

    def test_statement_for_value_error(self):
        self.assertRaises(ValueError, statement, {"customer": "BigCo", "performances": [{"playID": "hamlet", "audience": 25}]}, {"hamlet": {"name": "Hamlet", "type": "action"}})


if __name__ == "__main__":
    unittest.main()