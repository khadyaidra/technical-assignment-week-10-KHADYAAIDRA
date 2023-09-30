import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
from check_db import *
from payload import *

reader = SimpleMFRC522()

def rfid_read():
	id, text = reader.read()
	print(id)
	#print(text)
	print(type(id))
	result, status=checkid(id)
	
	if status == True:
		send_ubidots(result["id_card"], result["name"], result["kelas"])
		print("kartu terdaftar")
		results = "berhasil"
		return results;
	else:
		print("kartu tidak terdaftar")
		results = "gagal"
		return results;
		 
