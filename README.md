# Command to create the ssh:  kubectl create secret generic git-ssh-key-secret \
  --from-file=ssh-privatekey=/Users/your_user/.ssh/ \
  --type=kubernetes.io/ssh-auth \
  -n airflow
