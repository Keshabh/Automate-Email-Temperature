# Automate-Email-Temperature
Functioning:
--------------
The homepage shows the click link, that directs to django admin page. 
In Admin Page, there is an Automate_Email Table.
In Automate_Email Table, we have 4 attributes, Receiver_name, Email, City(with dropdown choices between ["Mumbai, Delhi, Chennai, Banglore, Kolkata"]), Time.
On feeding user details, it will automate email to the email id fed recently, about the temperature of the city the user has chosen, with an emoji depending upon how hot or cold temperature is.
The email subject is: "Hi {user name}, interested in our services".
The email body is: "{user city} TEMPERATURE: {city's current temperature} °C {emoji}
Emoji's used:
1. ☃️ if temperature is less than 10 degree celcius.
2. 🥶 if temperature is gerater than 10 and less than 15 degree celcius.
3. 🌞 if temperature is gerater than 15 and less than 25 degree celcius.
4. 😰 if temperature is gerater than 25 and less than 35 degree celcius.
5. 🔥 if temperature is greater than 35.

Steps
-----
1. Project is xtreme, then an app is made inside it naming 'Assignment'
2. In Assignment, admin page is registered in Assignment/admin.py.
3. In Assignment/models.py, ORM class is made to register the model for user that should contain, receiver's name, email, city, time.
4. Model is migrated, and the changes were reflected in admin page.
5. Users data can be filled from admin Page.
6. When new user data is feed into the table, using post signal, the new user email is returned in the models.py
   using @receiver, email is received in another function made new_user_data, which is calling home() function (retrieve's city temperature using weather API).
6. To Get the city's current temperature: OpenweatherMap API is used.
  I:   Account is made in OpenweatherMap.
  II:  In Assignment/models.py home() function, API key is merged with the OpenWeatherMap link and city's current temperature is receoved in json format.
  III: Json is converted into a dictionary.
  IV:  City's temperature is present inside nested dictionary: main > temp.
  V:   Temperature is received in Kelvin, then it is converted in celcius. [ # NOTE: 0 °C = - 273.15 K  ]
  VI:  Temperature in Celcius is passed to its caller function i.e new_user_data.
7. EMAIL HOST, PORT, USER, PASS is stored in xtreme/settings.py; It will be used in Assignment/models.py for sending mail to user.
   In Assignment/models.py, using send_mail() function , the message is sent to the user's email id received when new data is filled up in admin page.
   The message includes {Subject: 'Hi {user name}, interested in our services', Body: '{city} Temperature: {citys temperature in celcius} {emoji}}.
