# Electronic Health Record Manager

Implementation of web based software for handling electronic health records using Flask, html, CSS , bootstrap and mongodb to show high level implementation of blockchain.

![image](https://user-images.githubusercontent.com/47826916/128641182-ebd21ce0-10b9-437f-891b-7a576cf70932.png)


   Html+CSS+Bootstrap+JS has been utilized to create an intuitive website that allow users to login as admin, doctor or patient and perform their specific niche operations.
   The information collected to create a new medical record is based on the key points provided by the Ministry of Health and family welfare.

Blockchain implementation (Backend):
Flask, the micro framework in python is utilized for the implementation.

Information collected is stored in the cloud server (MongoDB) and a block is created with hash based on attributes of the medical record and it also holds the previous hash and timestamp of creation.

Note : No blockchain implementation is used. A custom highly level blockchain like architecture is developed to replicate the blockchain functionality. 

# Demo login

## PATIENT

Username : PAT001 

Password : password

## DOCTOR

Username : DOC1 

Password : password


## Use case diagram 

![image](https://user-images.githubusercontent.com/47826916/128641352-38af7184-4efb-4e1c-a592-538031a44f8a.png)

![image](https://user-images.githubusercontent.com/47826916/128641359-c2aa5e1c-2722-4a7e-b18a-d27ebc205045.png)


## Patient Record Access Schema 

![image](https://user-images.githubusercontent.com/47826916/129126551-ffdc286e-606f-4c51-bf50-715637710d7a.png)

## Guardian Mode Access Schema

![image](https://user-images.githubusercontent.com/47826916/129126608-edaf5ab1-e4fe-4826-9062-5556a0950ee5.png)

## Patient Data Blocks

![image](https://user-images.githubusercontent.com/47826916/129126680-9e069c60-ae40-4b86-9ad4-4991175db3a3.png)

## Patient Record Blocks

![image](https://user-images.githubusercontent.com/47826916/129126726-7aa3d8c3-422d-4598-a248-6491dd4277cf.png)

# Steps to run the project

Requirements : Python 3.x version

1. Clone the project to local directory
   
   <i>git clone https://github.com/antoprince001/Blockchain_for_EHR.git</i>
   
2. Change directory to cloned project 
 
   <i>cd Blockchain_for_EHR</i>
   
3. Install the pip module dependencies (Preferably in virtual enivironment)
   
   <i>pip install - r requirements.txt</i>
   
4. Then, run the main app.py file 

   <i>python app.py</i>
   
5. If you want to configure your own mongodb connection
   - Create an account in MongoDB Cloud atlas
   - Create a cluster and retrieve the connection url
   - Update the connection URL in Line 61 of app.py file

6. View the website live at http://localhost:5000/

