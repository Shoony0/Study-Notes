#!/bin/bash

SERVICE_NAME="my_web_service"
MAX_CPU_THRESHOLD=75  # In percentage
MIN_CPU_THRESHOLD=20
MAX_REPLICAS=10
MIN_REPLICAS=2

while true; do
  # Get the CPU usage (example using Docker Stats or Prometheus APIs)
  CPU_USAGE=$(docker stats --no-stream --format "{{.CPUPerc}}" $SERVICE_NAME | cut -d'%' -f1)

  # Get current replicas
  CURRENT_REPLICAS=$(docker service inspect --format "{{.Spec.Mode.Replicated.Replicas}}" $SERVICE_NAME)

  # Scale up if CPU usage exceeds threshold
  if (( $(echo "$CPU_USAGE > $MAX_CPU_THRESHOLD" | bc -l) )) && [ $CURRENT_REPLICAS -lt $MAX_REPLICAS ]; then
    NEW_REPLICAS=$((CURRENT_REPLICAS + 1))
    docker service scale $SERVICE_NAME=$NEW_REPLICAS
    echo "Scaled up to $NEW_REPLICAS replicas"
  fi

  # Scale down if CPU usage drops below threshold
  if (( $(echo "$CPU_USAGE < $MIN_CPU_THRESHOLD" | bc -l) )) && [ $CURRENT_REPLICAS -gt $MIN_REPLICAS ]; then
    NEW_REPLICAS=$((CURRENT_REPLICAS - 1))
    docker service scale $SERVICE_NAME=$NEW_REPLICAS
    echo "Scaled down to $NEW_REPLICAS replicas"
  fi

  sleep 10  # Check every 10 seconds
done
