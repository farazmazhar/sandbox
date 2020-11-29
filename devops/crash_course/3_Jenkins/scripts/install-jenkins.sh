#!/bin/bash
echo "Updating..."
sudo apt update -y
echo "Installing Java..."
sudo apt install -y openjdk-8-jdk
echo "Getting keys...?"
wget -q -O - https://pkg.jenkins.io/debian/jenkins.io.key | sudo apt-key add -
sudo sh -c 'echo deb http://pkg.jenkins.io/debian-stable binary/ > /etc/apt/sources.list.d/jenkins.list'
echo "Updating..."
sudo apt update -y
echo "Installing Jenkins..."
sudo apt install -y jenkins
echo "wot?"
systemctl status jenkins
