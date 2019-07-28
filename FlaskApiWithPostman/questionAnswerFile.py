# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 16:17:49 2019

@author: acer
"""

import flask
from flask import Flask,request
import json

app = Flask(__name__)


class ChatBot:
    
    def answer_queries(self,question,text=''):
        
        if 'name' in question:
            return "Shashank"
        elif 'age' in question:
            return "24"
        elif 'special' in question:
            return "anything"
  
@app.route('/home')
def home():
    return "Working api"
          
@app.route('/get_answers',methods=['GET','POST'])
def answer():
   queries = request.data.decode('utf-8') 
   dictionary = json.loads(queries)
   question,text = dictionary['question'], dictionary['text']
   chatBot = ChatBot()
   answer = chatBot.answer_queries(question,text )
   return answer

if __name__ =="__main__":
   app.run('localhost',port=5000)         # instead of localhost we can write 0.0.0.0 which will make it open for all