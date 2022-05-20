# Daily art newsletter

## Key points

* Parsed data from artistro.com that contains images of the works of art and their descriptions using Beatiful soup and requests
* Built a simple Python script to send emails from the gmail account
* Set the program to automatically send the emails to the specified receivers emails at a certain time each day

## Code and resources used

**Python Version:** 3.6

**Packages:** smtplib ssl schedule bs4 requests pickle time

**Resources** https://realpython.com/python-send-email/, artistro.com

## Future plans

* Update the parser to get the data from Wikipedia instead of artistro.com
* Make a simple db to store the subscribers and their emails
* Make a simple website (maybe with pywebio) to allow users to subscribe and unsubscribe from the newsletter
* Update the html, include option to unsubscribe
