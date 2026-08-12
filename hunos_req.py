import threading
import requests
import re




from hunos_cve import zep_cve
from hunos_cve import  think_cve
from  hunos_cve import  php_unit














def get_html(ip):


    php_unit(ip)  #test all ips  cve in phpunit




    try:


      
        resp  = requests.get( ip  , timeout=10)
       


        if (  re.search  ('Zeppelin'  , resp.text) ) :
                 
            zep_cve( ip )





        if  (  re.search   ( 'ThinkPHP'  ,  resp.text)  )  :

            
                 print('ThinkPHP   encontrado')


                 think_cve( ip )





    except Exception  as   e:

        print('' )
        










def teste():



 ptr = open('ips', 'r') 


 ips = ptr.readlines()




 for ip in ips:


    ip = ip.strip()    

    ip = 'http://' + ip

    
    t = threading.Thread(target=get_html  , args=(ip ,))

    t.start()






