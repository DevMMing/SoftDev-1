'''Duckers - Daniel Gelfand and Sophia Xu
SoftDev1 pd<6>
K<10> -- Jinja Tuning
2018-09-24'''

import csv #import csv module
from random import randint
from flask import Flask, render_template

with open('occupations.csv','r') as csvfile: #opens occupations.csv as a readable file saved as variable csvfile
    csvreader = csv.reader(csvfile) #reads the whole file
    next(csvreader) # doesn't read the header
    dict = {rows[0]:float(rows[1]) for rows in csvreader} #creates a dictionary where every even row is a key and every odd is a value
    dict.pop('Total') # removes the Total key from dict

app = Flask(__name__) #create instance of class Flask

def randJob():


    #select an integer from a range of 1-1000
    #If a job percentage is 5%, it takes up 50 spots in that range
    rand = randint(1,1000)

    lower = 0
    upper = 0
    # loop through the jobs
    for key in dict:

        # update the upper limit
        # multiplication by 10 to get rid of decimals
        upper += (dict[key]*10 + lower)

        # check if random int is within that job percentage range
        if(rand > lower and rand <= upper):
            return key
        else:
        #update the lower limit(placed here bc for first iteration lower should stay 0)
            lower += (dict[key]*10)


@app.route("/") #assign fxn to route
def hello_world():
    print(__name__)
    return render_template('test.html', collection = dict,randJob = randJob() , ctr = 0)


@app.route("/stuy")
def hello_stuy():
    return "GO STUY!"




if __name__ == "__main__":
    app.debug = True
    app.run()
