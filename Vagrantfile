Vagrant.configure(2) do |config|
    config.vm.box = "ubuntu/bionic64"
      
    # configure loadbalancer
    config.vm.define "load-balancer" do |loadbalancer|
      loadbalancer.vm.network "private_network", ip: "0.0.0.0"
      loadbalancer.vm.hostname = "load-balancer"
      loadbalancer.vm.network "forwarded_port", guest: 80, host: 8080
      loadbalancer.vm.provider "virtualbox" do |vb|
        vb.memory = 512
        vb.customize ["modifyvm", :id, "--audio", "none"]
      end
    end
    # configure web servers
    config.vm.define "server-1" do |server_1|
      server_1.vm.network "private_network", ip: "0.0.0.0"
      server_1.vm.hostname = "server-1"
      server_1.vm.provider "virtualbox" do |vb|
        vb.memory = 512
        vb.customize ["modifyvm", :id, "--audio", "none"]
      end
    end
    config.vm.define "server-2" do |server_2|
      server_2.vm.network "private_network", ip: "0.0.0.0"
      server_2.vm.hostname = "server-2"
      server_2.vm.provider "virtualbox" do |vb|
        vb.memory = 512
        vb.customize ["modifyvm", :id, "--audio", "none"]
      end
    end
    config.vm.define "server-3" do |server_3|
        server_2.vm.network "private_network", ip: "0.0.0.0"
        server_2.vm.hostname = "server-3"
        server_2.vm.provider "virtualbox" do |vb|
          vb.memory = 512
          vb.customize ["modifyvm", :id, "--audio", "none"]
        end
      end
    
    # update the packages on the VMs
    config.vm.provision "shell", inline: <<-SHELL
      apt-get update
    SHELL
 end