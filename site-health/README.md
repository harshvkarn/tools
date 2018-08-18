## Running

To run this script:
- Create Kubernetes secret
`kubectl create secret generic tokens --from-literal=token=<your-slack-token-here>` 

- Apply the health-check YAML
`kubectl apply -f site-check.yml`

 
