#!/usr/bin/env python3
# npuTemp.py
# - Jetson의 jtop 라이브러리를 사용하여 NPU 온도를 포함한
#   CPU, GPU, SoC 등의 온도를 주기적으로 CSV 파일에 기록
# - 기록 주기 및 출력 파일 경로는 상단에서 설정 가능
# - 출력 파일이 없으면 헤더 작성
# - jtop 라이브러리 설치: pip install jtop
# - 실행: python3 npuTemp.py


import csv, time, datetime, os
from jtop import jtop

OUTFILE = "~/jtop_log/jtop_temps.csv"   
INTERVAL_S = 1.0     

def ensure_dir(path):
    d = os.path.dirname(path)
    if d and not os.path.isdir(d):
        os.makedirs(d, exist_ok=True)

def main():
    ensure_dir(OUTFILE)
    with jtop() as jetson:
        temps = jetson.temperature
        fieldnames = ["timestamp"] + [f"temp.{k}" for k in sorted(temps.keys())]

        file_exists = os.path.isfile(OUTFILE)
        with open(OUTFILE, "a", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            if not file_exists:
                writer.writeheader()

            while jetson.ok():
        
                row = {"timestamp": datetime.datetime.now().isoformat()}
                temps = jetson.temperature
                for name, vals in temps.items():
                    row[f"temp.{name}"] = vals.get("temp")

                writer.writerow(row)
                f.flush()
                time.sleep(INTERVAL_S)

if __name__ == "__main__":
    main()