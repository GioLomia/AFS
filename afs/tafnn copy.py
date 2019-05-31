import requests, json
import datetime as dt
from time import sleep


class teller():
    

    def __init__(self, iteration=0, distribution=0, distrmessage = '0', maxiter=0, maxitermessage = '0', epochdistribution=0, epoch=0, epochmessage ='0', testloss=0, valloss=0, maxdelay =0, maxdelaydelta =0, maxdelaymessage = '0', profile_link='0'):

        self.iteration = iteration
        self.distribution = distribution
        self.distrmessage = distrmessage
        self.maxiter = maxiter
        self.maxitermessage = maxitermessage
        self.epochdistribution = epochdistribution
        self.epoch = epoch
        self.epochmessage = epochmessage
        self.testloss = testloss
        self.valloss = valloss
        self.maxdelay = maxdelay
        self.maxdelaydelta = maxdelaydelta
        self.maxdelaymessage = maxdelaymessage
        self.profile_link = profile_link


    def api(self,json_dump):

        '''
        Function for collection of the provided variables and strings and sending them combined as a 'GET' request
        to be distributed by Flask server later on.
        Takes one argument - 'json_dump', that basically is a stringified combination of dictionaries.
        '''

        # declare endpoint_url for GET request
        endpoint_url = "https://tafnn-flask.herokuapp.com"

        # send GET request, followed by json_dump argument
        requests.get(endpoint_url, json_dump)


    def unique_id(id):
            
            json_dump = json.dumps(str({1:{"Requesting Unique id":'0'}}))
            self.api(json_dump)
            requests.post(endpoint_url, json_dump)

            requests.get(endpoint_url, json_dump)




    def teller(self, iteration=0, distribution=0, distrmessage='0', maxiter=0, maxitermessage='0', epochdistribution=0, epoch=0, epochmessage='0', testloss=0, valloss=0, maxdelay=0, maxdelaydelta=0, maxdelaymessage='0', profile_link='0'):

        '''
        'teller' function takes maximum of 14 arguments. Default values are 0's.

        $iteration argument is for counting iterations. type = number.

        $distribution argument is basically a divider, for every how many iterations do you need to send the GET request. type = number.

        $distrmessage - your message after reaching specific number of iterations, when iterations % distribution == 0. type = string.

        $maxiter is a maximum of iterations, after which the model finishes training. Make sure to send +1, as long as
        python takes the 'y' from range(x , y) and finishes the loop when technically y = (y - 1). type = number.

        $maxitermessage is a message you want to send after reaching maxiter size. type = string.

        $epochdistribution is the same as 'distribution' argument, but for epochs. type = number.

        $epoch counts epochs. type = number.

        $epochmessage is sended after reaching number of epochs when epochs % epochdistribution == 0 . type = string

        $testloss takes test loss as an information. type = number.

        $valloss takes validation loss as an information. type = number.

        $maxdelay is maximum amount of delay, after which server will automatically tell you that something might be crashed,
        and you've to check the server. type = number.

        $maxdelaydelta is a maximum dynamic change of maxdelay. For instance, if maxdelay = 5 (5 seconds), and maxdelaydelta = 1,
        you won't be notified until the request is delayed for more than 6 seconds.
        In case you're saving checkpoint for every certain number of iterations, and it takes longer time than average iteration
        time, that's where you use 'maxdelaydelta' argument. type = number.

        $maxdelaymessage is a message for you to receive after reaching maximum time of delay.  type = string.

        $profile_link is a link of your Facebook profile, that will be used by the chatbot to send you all the information later on.
        type = string.

        '''

        # check if iteration != 0, and != maxiter, and iteration % distribution = 0.
        if iteration != 0 and iteration != maxiter and iteration%distribution == 0:
            json_dump = json.dumps(str({1:{str(iteration):str(distrmessage)}, 2:{'Profile Link':str(profile_link)}}))
            self.api(json_dump)

        # check if epoch != 0, and iteration != maxiter, and epoch % epochdistribution = 0.
        if epoch != 0 and iteration != maxiter and epoch%epochdistribution == 0:
            json_dump = json.dumps(str({1:{(epoch):str(epochmessage), 'Test Loss':str(testloss)}, 2:{'Validation Loss':str(valloss), 'Profile Link':str(profile_link)}}))
            self.api(json_dump)

        # check if iteration != 0, and != maxiter, and iteration % distribution = 0, epoch != 0, epoch % epochdistribution = 0.
        if iteration != 0 and iteration != maxiter and iteration%distribution == 0 and epoch != 0 and epoch%epochdistribution == 0:
            json_dump = json.dumps(str({1:{str(iteration):str(distrmessage), str(epoch):str(epochmessage)}, 2:{'Test Loss':str(testloss), 'Validation Loss':str(valloss)}, 3:{'Profile Link':str(profile_link)}}))
            self.api(json_dump)

        # check if iterations = maximum amount of iterations, i.e. "training the model has been finished"
        if self.iteration == self.maxiter:
            json_dump = json.dumps(str({1:{str(iteration):distrmessage}, 2:{str(epoch):str(epochmessage)}, 3:{str(maxiter):maxitermessage, 'Test Loss':str(testloss)}, 3:{'Validation Loss':str(valloss), 'Profile Link':profile_link}}))
            self.api(json_dump)


if __name__ == '__main__':

    # declare endpoint_url for GET request
    endpoint_url = "https://tafnn-flask.herokuapp.com"