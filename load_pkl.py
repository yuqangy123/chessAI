import pickle
import pickletools

with open("train_data_buffer.pkl", "rb") as file:
    while True:
        try:
            out={}
            pickletools.dis(file, out)
            a=0
            
        except EOFError:
            # 当文件读取完毕时退出循环
            break
        except Exception as e:
            # 处理其他异常
            print("读取文件时发生异常:", str(e))
            