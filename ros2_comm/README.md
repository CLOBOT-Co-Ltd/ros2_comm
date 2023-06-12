# ROS2COMM

## Install Zyre Python Bindings

### Install ZMQ Libraries

```bash
echo "deb http://download.opensuse.org/repositories/network:/messaging:/zeromq:/release-stable/Debian_9.0/ ./" >> /etc/apt/sources.list
wget https://download.opensuse.org/repositories/network:/messaging:/zeromq:/release-stable/Debian_9.0/Release.key -O- | sudo apt-key add
sudo apt-get install libzmq3-dev
```

### Install czmq python bindings

```bash
git clone https://github.com/zeromq/czmq.git

cd czmq/bindings/python

python3 setup.py build
sudo python3 setup.py install
```

### Install zyre python bindings

```bash
git clone https://github.com/zeromq/zyre.git

cd zyre/bindings/python

python3 setup.py build
sudo python3 setup.py install
```
