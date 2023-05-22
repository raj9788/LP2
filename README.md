CCL
to run
python3 path_to_google_sdk/bin/devapp_server.py  path_to_project_folder/

incase python3 doesn't work try onlu python instead of python3


WADL

npm i


to run angular
ng serve

to run node codes
npm init
npm install dependecy
node main_file.js  or nodemon main_file.js





To Transfer files between two files 
first keep the nat network as it is then run this commands
sudo apt install net-tools
sudo apt install openssh-server
sudo apt install openssh-client


run this on both machines
after running close both machines
change the nat to nat network in both machines
then run both machines
run 
ifconfig
on both check 3rd line of inet both ip address should be different if same file transfer will not work
if different
then run
scp filename.txt pc2username@pc2ipaddress:/home/pc2username/Desktop
after running if a prompt occurs on terminal 1 type yes
this will transfer the file and the file willbe visible on the desktop of pc2

