# Calorie Tracker
🔊 Track your daily calorie consumption with calorie tracker

## 🤔About The Project
Tracking your daily calorie consumption helps you in maintaining good diet and physical health. Using calorie tracker you can keep track of your daily calorie consumption.
## 💡Features
##### The features offered by this app are:
1. New users can signup.                                                                                                             
2. Add data about their daily calorie consumption.                                                                                                                    
3. Users can see their data and get a mail describing their calorie consumption history in a graph. 
4. Admins can see users data and can also delete a particular user.
5. jwt tokens are used for authorization and access to specific api's is allowed based on the user roles.
## 🏃How to get it up and running
1. You can download it or clone it in your terminal by typing `git clone https://github.com/manoj-b-b/Task-2-Api.git`
2. Install python 3.9 and pip3
3. Install the requirements present in the requirements.txt by typing the command `pip3 install requirements.txt`                                                      
4. Create a connection in mongodb, with a new database.
5. Create a collection called users.
6. Setup your mail configurations with the help of [flask_mail](https://pythonhosted.org/Flask-Mail/) and mention JWT_SECRETE_KEY in main app.
7.Command to run the app - `flask run`
## Testing api's
1. make use postman to test api
2. while making request - go to authorization tab, select bearer token and paste the token.
## 📚Tech Stack
### Backend tech stack
* [Flask](https://flask-doc.readthedocs.io/en/latest)                                                                                                             
* [MongoDB](https://docs.mongodb.com)
