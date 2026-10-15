**weather-and-wear**
---
command-line tool written in python that fetches live weather data for any city and proposes based on that what you should wear without the need of any API-key



**How it works**
---
The tool runs entirely in the terminal and is built with a modular architecture to ensure that any user can easily and quickly change or add functions that they want:
1. Takes a city name and converts it into latitude and longitude using the Open-Meteo Geocoding API[^1]
2. Takes live temperature and wind speed from the Open-Meteo Forecast API[^1]
3. Isolates the needed bit of the data that it works with
4. Applies windchill formula to calculate the effective temperature
5. Recommands what the user should wear

[^1]:https://open-meteo.com/

**Roadmap**
---
- [x] Integration of Open-Meteo APIs
- [x] Data Isolation
- [x] Safety check for user error or missing cities in the Open-Meto API
- [x] Implementation of windchill formula 
- [x] Rule-Based clothing recommandation module
- [x] Better experience navigating the main.py file for better modular access
-  Implementation of precipation/rain data from another API
-  German and french language options
-  Saves the last used city for quicker use
-  User Interface and executable programm for windows/linux/mac/freebsd



**Installation and Running**
---
1. Clone the repo
```bash
git clone https://github.com/julienvtrx/weather-and-wear.git
cd weather-and-wear
```

2. Create and activate venv (recommended)
>Windows
```bash
python -m venv venv
.\venv\Scripts\Activate.ps1
```
>Linux/macOS
```bash
python -m venv venv
source venv/bin/activate
```
3. Install dependencies
```bash
pip install -r requirements.txt
```
4. Run the tool
```bash
python main.py
```




**Inspiration**
---
I saw a video where someone made a program to catch the right train to take a chain of subways without having to wait and as he left his flat he had to walk back up as it was way colder than he expected.  
I thought it would be a great idea if he would add a program that tells him what to wear to his program as then he wouldnt have to run his way back to his flat to get his jacket (lol).    
So here i am coding that little idea.



**Contact**
---
If you:  
- have any question  
- just want to talk about the project  
- have an idea for the future of the project  

dont mind hitting me up!  
email: vantouroux.julien@gmail.com
