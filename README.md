# check-JetsonOrin-Temperature
> Jetson Orin의 cpu, gpu 등의 온도를 측정, CSV 파일로 저장 및 그래프로 확인 가능한 프로그램

------------
## 사용 방법
### **1. 먼저 필요한 라이브러리들을 설치해준다**
```
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install python-pip
pip install pandas matplotlib jtop
pip install jtop
sudo -H pip install -U jetson-stats
```

### **2. 재부팅 후 진행한다**
```
sudo reboot
```

### **3. 리포지토리를 터미널에서 복사해준다.**
```
git clone https://github.com/beakdongH/check-JetsonOrin-Temperature 
```

### **4. 파일이 있는 폴더로 들어가준다.**
```
cd check-JetsonOrin-Temperature/temper
```
### **5. 온도 측정을 시작한다.**
```
python3 npuTemp.py
```

### **6. 온도 측정을 완료했다면, ESC 또는 Ctrl+C를 눌러 종료시킨 후, 그래프(plot)을 그린다.**
```
(ESC / Ctrl+C)
python3 pltnpuTemp.py
```
