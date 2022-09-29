# Create multiple nodes using virtual box

- create a custom network adapter under File -> Network adapter creation
- pick the network ip address. It shoudl be something like *192.168.X.Y*
- for each VM:
  - go to settings and on the second netork adapter select the *host only* and then the newly created network adapter at the step above
  - open the VM, create a file called *network-config.yaml* under */etc/netplan* with this content (spaces/indentation are relevant):
    
    ```
    ethernets:                                                                                                                  
      enp0s3:                                                                           
        dhcp4: yes
      enp0s8:
        dhcp4: false
        addresses: ["192.168.X.Y"]
    version: 2
    ```
  
  where X is the same number from the net adapter creation; Y is starting from 111 for the first machine, 112 for the second etc. etc.
  
  - run
    
        netplan apply
  
  - ping the other machines to see if connection works.




# Deploy swarm

    docker stack deploy -c stack.yaml student_app

# Visualize cluster

	  docker service create --name=viz --publish=8080:8080/tcp --constraint=node.role==manager --mount=type=bind,src=/var/run/docker.sock,dst=/var/run/docker.sock dockersamples/visualizer

# Deploy registry service

    docker service create --name registry --publish published=5000,target=5000 registry:2

# Build and push image
    
    docker-compose build
    docker-compose push