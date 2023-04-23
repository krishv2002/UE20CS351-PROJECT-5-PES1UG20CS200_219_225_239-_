#!/bin/bash
minikube start
@FOR /f "tokens=*" %i IN ('minikube docker-env --shell cmd') DO @%i
docker build -t flaskapp .
kubectl apply -f secret.yaml 
kubectl apply -f configmap.yaml
kubectl apply -f services.yaml
kubectl apply -f deployments.yaml
minikube service mongo-express-service 
#open in new terminal
minikube service flask-app-service
