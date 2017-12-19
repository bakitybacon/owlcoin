OwlCoin
=======

OwlCoin is an ENGI 120 team at Rice University. We aim to create a low-cost cryptocurrency mining device for distribution to high schools and colleges around the country to expose more people to this world-altering technology.

This software enables the user to connect to a cryptocurrency network and mine OwlCoin. It facilitates this by using multiple methods of user interaction:

* a screen that indicates the balance of cryptocurrency in the user's wallet, as well as any other pertinent messages
* a red LED that is used to indicate errors
* a green LED to indicate that the device is currently running, to ensure safe shutdown


In order to use this repository, it is necessary to have access to the OwlCoin mining network. We cannot allow this, as it would conflict with the goals of our device.

Here are a few pictures of OwlCoin in action:

![In Use](https://github.com/bakitybacon/owlcoin/blob/master/owlcoininuse.jpeg)
![Wiring](https://github.com/bakitybacon/owlcoin/blob/master/owlcoinwiring.jpeg)

And, here's the video of our prototype in action:

https://youtu.be/EflcxropQAA

Technical details are available in this document:

[Technical Information](https://github.com/bakitybacon/owlcoin/blob/master/technicaldetails.pdf)

The last iteration of the software focused on instantaneous responses to errors and constant updating, as well as an asynchronous approach to LED management. It uses interprocess communication to implement asynchronicity, as when an error is found, a signal is sent to the LED handler script which triggers the LED. This is a marked contrast with earlier iterations that updated the screen once per minute, which means an error could occur and not be obvious for up to a minute. 

In the future, the following changes should be made:
* Occasionally, the device does not show the shutdown message, if the shutdown message is overwritten by the `update_display_asynch.py` script before the shutdown is complete. This can be fixed if the shutdown script kills the the script.
* Actually, the LED handler script doesn't really need to exist. The signals can be sent directly from the bash script.
* Deleting the Threading used in the `asynchleds.py` script, which does not need to occur. I thought I needed it, but the real issue was global/local variables in python.

OwlCoin consists of the following members:
* Lon Kai Pang
* Charlie Benninger
* Mojola Balogun
* Zac Zalles
* Corrin Fosmire

