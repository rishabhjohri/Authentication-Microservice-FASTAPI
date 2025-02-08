#Steps to setup : 

1) Download and install virtualbox
2) Download lubuntu : lubuntu-24.04.1-desktop-amd64.iso
3) Create 2 VMs : server and datacenter
   Configuration :
   ![Alt Text](images/server.png)
   
   ![Alt Text](images/datacenter.png)

   Note : for downloading and building the docker image , we want the VMs to be able to access the Internet so keep network type as  : NAT
          once , this microservice is setup and its time to test , we want these VMs to communicate with each other : So , connection type = Host only

4) Install lubuntu in both VMs ( pretty standard installation ;) , keep everything default , just click next !)
5) Once the lubuntu stuff is done , dont forget to save the state of VMs)
   Do this for both VMs :
   5.1> Install docker : (NOTE : if it's showing permission denied use sudo before every command)
   
        sudo apt update && sudo apt install -y docker.io
   
   For datacenter VM:
   5.2> Install mongodb  using docker and run it as a container :
   
         # Pull MongoDB Docker image
         docker pull mongo:4.2
            
         # Run MongoDB container
         docker run -d --name mongodb -p 27017:27017 -e MONGO_INITDB_ROOT_USERNAME=admin -e MONGO_INITDB_ROOT_PASSWORD=adminpass --restart unless-stopped mongo:4.2
         # Verify if MongoDB is running:
         docker ps
         docker exec -it mongodb mongo
         #NOTE : Abobe command will start mongo shell -> To quit the shell , type quit()

   For server VM:
   5.3>
   
         git clone https://github.com/rishabhjohri/Authentication-Microservice-FASTAPI.git
         
         cd Authentication-Microservice-FASTAPI

         docker build -t auth-service .

   Switch to Host only connection now

 


   
