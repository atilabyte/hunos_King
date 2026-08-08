import threading
import requests
import re


from hunos_cve import CVE






def get_html(ip):



    try:


        

      
        resp  = requests.get( ip  , timeout=5)


        if (  re.search  ('<title>OpenCode</title>'  , resp.text) ) :
    

                 
            CVE( ip )





    except Exception  as   e:

        print('erro em '  + ip )
        













ptr = open('ips', 'r') 


ips = ptr.readlines()





for ip in ips:



    ip = ip.strip()    

    ip = 'http://' + ip

    

    t = threading.Thread(target=get_html, args=(ip,))

   

    t.start()






