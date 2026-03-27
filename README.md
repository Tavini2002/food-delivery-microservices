# Food Delivery System - Microservices😋🍉🍒🍔🍟🍕

## Steps to do

### Step 01: Switch to your branch

    1.   git checkout <your-branch-name>
    2.   git pull origin <your-branch-name>

### Step 02: Go to your folder

    3.   Example: cd <restaurant-service>

### Step 03: Setup Python and Install

    4.   python -m venv venv  / py -m venv venv
    5.   venv\Scripts\activate
    6.   pip install fastapi uvicorn pydantic httpx


### Step 04: Create Files inside the service folder

    * main.py
    * models.py
    * service.py
    * data_service.py

### Step 05: You have to find the code to be added to these files

### Step 06: Run your service in the browser 

    uvicorn main:app --reload --port 8002
    open http://localhost:8002/docs       ---->  🎉 You’ll see Swagger UI


### Step 07: Test APIs - GET/ POST/ PUT/ DELETE

### Step 08:  How to add gateway

**Client → API Gateway → Services**

   #### 1. cd gateway
   #### 2. python -m venv venv
   #### 3. venv\Scripts\activate
   #### 4. pip install fastapi uvicorn httpx
   #### 5. In main.py file --> add only url which is related to you
   
        SERVICES = {
            "user": "http://localhost:8001",
            "restaurant": "http://localhost:8002",
            "menu": "http://localhost:8003",
            "order": "http://localhost:8004",
            "delivery": "http://localhost:8005",
            "payment": "http://localhost:8006"
        }

   #### 6. Add routes
        Ex:-->  @app.get("/gateway/menu")