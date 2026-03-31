@echo off
echo Starting Payment Microservice on port 8006...
start cmd /k "python payment\main.py"

echo Starting API Gateway on port 8000...
start cmd /k "python gateway\main.py"

echo Both services are starting...
echo Once they are up, check:
echo - Gateway Swagger: http://localhost:8000/docs
echo - Payment Swagger: http://localhost:8006/docs
pause
