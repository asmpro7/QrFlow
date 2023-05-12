# -*- coding: utf-8 -*-

import sys,os
parent_folder_path = os.path.abspath(os.path.dirname(__file__))
sys.path.append(parent_folder_path)
sys.path.append(os.path.join(parent_folder_path, 'lib'))
sys.path.append(os.path.join(parent_folder_path, 'plugin'))

from flowlauncher import FlowLauncher
import qrcode
import random
import glob

class QrFlow(FlowLauncher):

    def query(self, query):
        output=[]
        if len(query.strip()) == 0:
                output.append({
                    "Title": "Enter value to generate a QR",
                    "IcoPath": "Images/app.png"})
        
        elif query=="clear|":
            files = glob.glob('QR/*')
            for f in files:
                os.remove(f)
            output.append({
                    "Title": "All QRs removed",
                    "IcoPath": "Images/cle.png"})
        else:
            na=random.randint(10000,99999)
            img=qrcode.make(query)
            img.save(f"QR\\QrFlow_{na}.png")
                       
            output.append({
                    "Title": "Click to open",
                    "IcoPath": f"QR\\QrFlow_{na}.png",
                    "JsonRPCAction": {"method": "open", "parameters":[f"QR\\QrFlow_{na}.png"]  }
                    })
            output.append({
                    "Title": "Click to open location",
                    "SubTitle": f"QrFlow_{na}.png",
                    "IcoPath": f"QR\\QrFlow_{na}.png",
                    "JsonRPCAction": {"method": "loca", "parameters":[f"QR\\QrFlow_{na}.png"]  }
                    })
    
        return output
    def open(self,QRF):
         os.startfile(QRF)

    def loca(sef,file_path):
        abs_file_path = os.path.abspath(file_path)
        os.startfile(os.path.dirname(abs_file_path))    

    def context_menu(self, data):
        return [{"Title": "Use: ' clear| ' to remove all QRs","IcoPath": "Images/app.png"}]

if __name__ == "__main__":
    QrFlow()
