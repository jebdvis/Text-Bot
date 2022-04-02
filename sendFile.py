import requests, bs4, smtplib, json

person = {'person',['1234567890', 'verizon']}

carriers = {
	'att':    '@txt.att.net',
	'tmobile':' @tmomail.net',
	'verizon':  '@mypixmessages.com',
	'sprint':   '@page.nextel.com'
}

def getSchedule():
    url = 'http://wadaily.co'
    res = requests.get(url)
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    numBlock = res.text.count('<div class="flex items-center">')
    numBlock = numBlock - 2
    blockLst = []
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    for i in range(numBlock):
        blockLst.append(soup.select('#__next > div.grid.box-border.px-8.md\:grid-cols-2.grid-cols-1 > div:nth-child(1) > div:nth-child(' + str(i+1) + ')> div > p.text-3xl.font-medium'))
    for i in range(len(blockLst)):
        blockLst[i] = blockLst[i][0].getText()
    returnStr = '\nSchedule: '
    for i in range(len(blockLst)):
        returnStr += ('\n' + blockLst[i])

    return returnStr
  
def getWeather(city_name, base_url = "https://api.openweathermap.org/data/2.5/weather?q=", api_key = "47b5dc0e681844647078f083aec2b715"):

    
    complete_url = base_url + city_name + "&appid=" + api_key + '&units=imperial'

    response = requests.get(complete_url)
    x = response.json()
    
    if x["cod"] != "404":
        y = x["main"]
        current_temperature = y["temp"]
        min_temp = y["temp_min"]
        max_temp = y["temp_max"]
        current_humidity = y["humidity"]
        z = x["weather"]
        weather_description = z[0]["description"]
        returnstr = "\nWeather:" + str("\nCurrent temperature: " + str(current_temperature) +"\nLow of the day: " +     str(min_temp) + "\nHigh of the day: " +str(max_temp)+"\nHumidity (%): " + str(current_humidity) + "\nDescription: " + str(weather_description))
        return returnstr
    else:
        return (" City Not Found ")


def send(person, message):
        # Replace the number with your own, or consider using an argument\dict for multiple people.
	to_number = person[0] + carriers[person[1]]
	auth = (<email>, <password>)

	# Establish a secure session with gmail's outgoing SMTP server using your gmail account
	server = smtplib.SMTP( "smtp.gmail.com", 587 )
	server.starttls()
	server.login(auth[0], auth[1])

	# Send text message through SMS gateway of destination number
	server.sendmail( auth[0], to_number, message)






def doTheThing(event = None, context = None):
    for i in person.keys():
        send(person[i], getWeather(<city>))
        send(person[i], getSchedule())

