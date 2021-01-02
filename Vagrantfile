# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure("2") do |config|
 # The most common configuration options are documented and commented below.
 # For a complete reference, please see the online documentation at
 # https://docs.vagrantup.com.

 # Every Vagrant development environment requires a box. You can search for
 # boxes at https://vagrantcloud.com/search.
 config.vm.box = "ubuntu/bionic64"
 config.vm.box_version = "~> 20200304.0.0"
 #Line 16 pins ubuntu/bionic64 to a specific version to avoid any updates to this image.

 config.vm.network "forwarded_port", guest: 8000, host: 8000
 #Line 19 maps a port from our local machine to the machine on our server, so when we run our application, we'll be running it on a network port 8000, and we want to make this port accessible from our host machine. So the host machine is our laptop or whichever machine you're running the development server on, and the guest machine is the development server itself. By default ports are not automatically accessible on any guest machine, so you need to add this line to make them accessible, so we can access them by going localhost port 8000, and it will automatically map the connection to our guest machine or development server.

#the provision block bellow allows you to run scripts when you first create your server. Line 24 and 25 are commands to disable the auto update, which conflicts with the line 27 auto update when we first run it on Ubuntu. The line 27 auto update will update the local repository with all of the available packages, so that we can install Python3 virtual env and zip. The next creates a bash aliases file and sets the Python3 to the default Python version for our Vagrant user, meaning every time you run Python it will automatically use Python3 instead of the default Python2.7.
 config.vm.provision "shell", inline: <<-SHELL
   systemctl disable apt-daily.service
   systemctl disable apt-daily.timer
 
   sudo apt-get update
   sudo apt-get install -y python3-venv zip

   touch /home/vagrant/.bash_aliases
   if ! grep -q PYTHON_ALIAS_ADDED /home/vagrant/.bash_aliases; then
     echo "# PYTHON_ALIAS_ADDED" >> /home/vagrant/.bash_aliases
     echo "alias python='python3'" >> /home/vagrant/.bash_aliases
   fi
 SHELL
end