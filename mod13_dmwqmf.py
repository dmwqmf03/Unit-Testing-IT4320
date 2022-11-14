import unittest
from datetime import datetime

# Unit Tests for Project 3 Inputs
# 1. symbol: capitalized, 1-7 alpha characters
# 2. chart type: 1 numeric character, 1 or 2
# 3. time series: 1 numeric character, 1 - 4
# 4. start date: date type YYYY-MM-DD
# 5. end date: date type YYYY-MM-DD

class UnitTest(unittest.TestCase):

    def testSymbol(self):
        charSymbol = input('\nEnter stock symbol: ')
        self.assertLessEqual(len(charSymbol), 7, msg="Error: Stock symbol is greater than seven alphabetical characters.")
        self.assertTrue(charSymbol.isupper(), msg="Error: Stock symbol is lowercase.")
        self.assertTrue(type(charSymbol) == int, msg="Error: Stock symbol input only accepts characters.")
        
    def testChartType(self):
        chartType = 1
        chartType = int(input('\nEnter your choice of chart type. Choose between 1 or 2: '))
        self.assertIn(chartType, [1,2], msg="Error: Choose between 1 or 2. No outside values are allowed.")

    def testTimeSeries(self):
        timeSeries = 1
        timeSeries = int(input('\nEnter time series option. Choose between 1-4: '))
        self.assertIn(timeSeries, [1,2,3,4], msg="Error: Choose between 1-4. No outside values are allowed.")

    def testStartDate(self):
        startDate = input('\nEnter the start date (format: YYYY-MM-DD): ')
        self.assertTrue(datetime.strptime(startDate, "%Y-%m-%d"))

    def testEndDate(self):
        endDate = input('\nEnter the end date (format: YYYY-MM-DD): ')
        self.assertTrue(datetime.strptime(endDate, "%Y-%m-%d"))

if __name__ == "__main__":
    unittest.main()