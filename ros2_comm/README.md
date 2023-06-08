# ROS2COMM

## Install Zyre

```bash
echo "deb http://download.opensuse.org/repositories/network:/messaging:/zeromq:/release-stable/Debian_9.0/ ./" >> /etc/apt/sources.list
wget https://download.opensuse.org/repositories/network:/messaging:/zeromq:/release-stable/Debian_9.0/Release.key -O- | sudo apt-key add
sudo apt-get install libzmq3-dev
sudo apt-get install libczmq-dev
```

```bash
# Run this following command in the 'src' directory
git clone https://github.com/zeromq/zyre.git

# build
source /opt/ros/[rosdistro]/setup.bash
colcon build
```