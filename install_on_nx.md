## 啟動板子前的準備
按照[Nvidia](https://developer.nvidia.com/embedded/learn/get-started-jetson-xavier-nx-devkit)的開發文件執行下列步驟，來啟動Jetson Xavier NX Developer Kit。

準備SD卡，於[Nvidia官網](https://developer.nvidia.com/embedded/jetpack)下載ISO檔燒錄至SD卡中。
## 準備環境
當成功開機後並且完成第一次開機的設定，我們需要準備相關的系統環境來運行我們的辨識系統。
1. 更新系統相關package
``` bash
sudo apt-get update
sudo apt-get upgrade
```
2. 安裝python3 & pip
``` bash
sudo apt-get install python3 python3-pip python3-numpy
```
3. 安裝tensorflow所需之系統檔案
```
sudo apt-get install libhdf5-serial-dev hdf5-tools libhdf5-dev zlib1g-dev zip libjpeg8-dev liblapack-dev libblas-dev gfortran
```
4. 安裝python相關的package
```
sudo pip3 install -U pip testresources setuptools==49.6.0 
sudo pip3 install -U --no-deps numpy==1.19.4 future==0.18.2 mock==3.0.5 keras_preprocessing==1.1.2 keras_applications==1.0.8 gast==0.4.0 protobuf pybind11 cython pkgconfig
```
5. 安裝Jpack 4.6版本的tensorflow
```
sudo pip3 install --pre --extra-index-url https://developer.download.nvidia.com/compute/redist/jp/v46 tensorflow
```
上述步驟執行完成後，可以透過在python code中import tensorflow來確定是否安裝成功。
在終端機中執行
```
python3
```
載入TensorFlow:
```
>>> import tensorflow as tf
tf.test.is_gpu_available()
```
上述命令將會正確的載入tensorflow的package，並且確定GPU可以正常使用。

## 啟用SSH Service
```bash
sudo apt-get install openssh-server
sudo systemctl enable ssh
sudo systemctl start ssh
```
## 啟用遠端桌面
設定xrdp遠端桌面
1. 安裝tightvncserver跟xrdp套件，重啟Jetson Nano
```
sudo apt update
sudo apt-get install tightvncserver xrdp
sudo reboot
```
2. 安裝xubuntu-desktop
```
sudo apt-get install xubuntu-desktop
```
3. 將xfce4-session寫入.xsession中
```
echo xfce4-session >~/.xsession
```
4. 重啟xrdp服務
```
sudo service xrdp restart
```

## 安裝Jtop監控工具
此工具可查看CPU與GPU相關資訊如溫度與功耗，也能將目前安裝的library顯示出來。
```
sudo apt-get install python-pip python-dev build-essential 
sudo pip install --upgrade pip
sudo -H pip install jetson-stats
```
執行此工具則運行
```
sudo jtop
```
## Reference
https://yanwei-liu.medium.com/nvidia-jetson-nano%E5%AD%B8%E7%BF%92%E7%9B%AE%E9%8C%84-645ddeed1704
https://docs.nvidia.com/deeplearning/frameworks/install-tf-jetson-platform/index.html#prereqs
