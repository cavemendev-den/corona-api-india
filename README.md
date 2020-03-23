# corona-api-india

<h1> Setup </h1>
<ol>
<li>Clone the Project</li>
<li>Create a virtual environment</li>
<li>Install all packages from the requirements.txt file </li>
<li>Go to cmd/terminal start the server</li>
</ol>

<h4> Details </h4>

```
git clone https://github.com/cavemendev-den/corona-api-india.git
vitualenv venv
source venv/bin/activate
pip3 install -r requirements.txt
cd corona-api-india
python3 manage.py runserver
```

<h3>APIs</h3>
To get overall country wide information i.e Number of passengers screened at airports,Active cases,<br>
cured or discharged cases,death cases,Migrated covid 19 patients

> URL : http://127.0.0.1:8000/api/get-head/ <br>

Json Response 

```
{
  "Passengers screened at airport": "15,17,327", 
  "Active COVID 2019 cases": "415", 
  "Cured/discharged cases ": "23", 
  "Death cases ": "7", 
  "Migrated COVID-19 Patient ": "1"
}

```
To get statewise information. We get the followings data : id,state name, confirmed cases (indian),confirmed cases (foreign) <br>
cured/discharged, death <br>
> url http://127.0.0.1:8000/api/get-states/ 

Takes one GET parameter `states`

If you need all states data at once you can pass <b>all</b> as the value to the get parameter : 
> url http://127.0.0.1:8000/api/get-states/?states=all

If you need particular states you can pass an array of state ids according to the table given at the end : 
> url http://127.0.0.1:8000/api/get-states/?states=["1","2","3"]



```
{
  "id": "1", 
  "Name of State / UT": "Andhra Pradesh",
  "Total Confirmed cases (Indian National)": "5", 
  "Total Confirmed cases ( Foreign National )": "0", 
  "Cured/Discharged/Migrated": "0", 
  "Death": "0"
}
```

<h3> State id reference Table </h3>

| State / UT Name | id |
|------------------|---|
|Andhra Pradesh|1|
 
