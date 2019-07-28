"""
This Class calculates the Standard Deviaiton.
Parameters
----------------------------------------
output: Mtandard deviation of the array
----------------------------------------
"""
import flask
from flask import Flask,request
import json

app = Flask(__name__)

class StandardDeviation:
    """
        calculateMean method calculates mean of an integer array.

        Parameters
        ----------------------------------------
        input : Integer array

        output: Mean of that array
        ----------------------------------------
    """
    def calculateMean(self, numberArray):
        sumOfArray = 0
        for i in numberArray:
            sumOfArray = sumOfArray+i
        return sumOfArray/len(numberArray)
    """
        standardDeviation method calculates standard deviation of an integer array.
        Parameters
        ----------------------------------------
        input : Integer array

        output: Standard deviation of the array
        ----------------------------------------
    """
    def standardDeviation(self, numberArray):
        sumOfArray = 0
        meanOfArray = self.calculateMean(numberArray)
        for i in numberArray:
            sumOfArray = sumOfArray + ((i-meanOfArray)**2/len(numberArray))
        return sumOfArray**0.5


std = StandardDeviation()
print('Standard Deviation = ' ,std.standardDeviation([2,6,6,5,4,8,2,1,1,0,25]))


@app.route('/home')
def test_api():
    return "Api is working"

@app.route('/standardDeviation')
def calculateStandardDeviation():
   arr = request.data.decode('utf-8') 
   jsonStr = json.loads(arr)
   arr = jsonStr['arr']
   std = StandardDeviation()
   std.standardDeviation(arr)
   
if __name__ =="__main__":
    app.run('0.0.0.0',port=5000)

