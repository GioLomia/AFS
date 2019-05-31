# AFS

[![N|Solid](https://alpes.cloud/up/04f421c9980ab436d97dd6a910bcaf49.svg)](https://www.systemcorp.ai)



[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)]()

AFS is a Python based library, that helps Deep / Machine Learning specialists to track their models during
training without accessing server, and getting notifications full of their desired information via beloved
Social Media platforms.

[![N|Solid](https://alpes.cloud/up/32bddf91ffdf1fc2a66614f8a2fbbdaa.png)](https://www.systemcorp.ai)




# PROS
  - Built as lightweight as possible
  - Takes 14 arguments, therefore users can check almost everything while their model is training
  - Back-End is built on Flask framework, and open-sourced. You can contribute to implement more
  Social Media platforms' APIs.

# TODO

  - Finish working on Back-End for Facebook Messenger.

### Used Frameworks & Libraries

AFS is built totally on Python technology.

* [Python 3] - for library building
* [Flask] - for Back-End


### Installation

Python 3.6+ required to use.

Get the package from [PyPi]

```sh
$ pip install AFS
```



### Usage

Import the AFS and reach 'teller' function.
Define the AFS.teller function inside the training loop, and pass the arguments.

```sh
$ import AFS as afs
$ afs.teller(arg1, arg2)
```



# Arguments

```sh

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

  $profile_link is a link of your Facebook profile, that will be used by the agent to send you all the information later on.
  type = string.
```


# JSON Instance

The API sends the JSON array, that is basically stringified version of combination of dictionaries.


# Implementations

  The Flask server is deployed on Heroku, and implemented only in Facebook Messenger for now.
  Next Social Media Platforms:

  - [Slack]
  - [Discord]



### TODOs

    - Finish working on Back-End for Facebook Messenger.


License
----

BSD 3-Clause Licence




[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)


   [dill]: <https://github.com/joemccann/dillinger>
   [git-repo-url]: <https://github.com/joemccann/dillinger.git>
   [john gruber]: <http://daringfireball.net>
   [df1]: <http://daringfireball.net/projects/markdown/>
   [markdown-it]: <https://github.com/markdown-it/markdown-it>
   [Ace Editor]: <http://ace.ajax.org>
   [node.js]: <http://nodejs.org>
   [Twitter Bootstrap]: <http://twitter.github.com/bootstrap/>
   [jQuery]: <http://jquery.com>
   [@tjholowaychuk]: <http://twitter.com/tjholowaychuk>
   [express]: <http://expressjs.com>
   [AngularJS]: <http://angularjs.org>
   [Gulp]: <http://gulpjs.com>
   [OpenCV]: <https://opencv.org>
   [Single Shot Detection (SSD)]: <https://arxiv.org/pdf/1512.02325.pdf>
   [ResNet50]: <https://arxiv.org/pdf/1512.03385.pdf>
   [Python 3]: <https://python.org>
   [Flask]: <http://flask.pocoo.org>
   [PyPi]: <https://pypi.org>
   [Slack]: <https://slack.com>
   [Discord]: <https://discordapp.com>

   [PlDb]: <https://github.com/joemccann/dillinger/tree/master/plugins/dropbox/README.md>
   [PlGh]: <https://github.com/joemccann/dillinger/tree/master/plugins/github/README.md>
   [PlGd]: <https://github.com/joemccann/dillinger/tree/master/plugins/googledrive/README.md>
   [PlOd]: <https://github.com/joemccann/dillinger/tree/master/plugins/onedrive/README.md>
   [PlMe]: <https://github.com/joemccann/dillinger/tree/master/plugins/medium/README.md>
   [PlGa]: <https://github.com/RahulHP/dillinger/blob/master/plugins/googleanalytics/README.md>
