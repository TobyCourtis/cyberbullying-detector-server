# cyberbullying-detector-server
Server component of the 'Cyberbullying Detector'
<br></br>
My research paper titled ‘Towards Automated Blocking of Cyberbullying in Online Social Networks’, outlining the background and approach to producing my cyberbullying detector can be viewed [here](http://www.tobycourtis.com/wp-content/uploads/2020/04/Towards-Automated-Blocking-of-Cyberbullying-in-OSNs.pdf).
<br></br>
Experiment by inputting text to the Cyberbullying Detector through the Google Chrome extension user interface [here](http://www.tobycourtis.com/index.php/cyberbullying_detector/). This online tool uses the latest build of the cyberbullying-detector-server. 

How to run the Server:

1) Aquire SSL Certificates if requiring https
   - Label 'cert.pem' and 'key.pem' then transfer into 'ssl_certificates' directory
2) Download large (2GB) vectors file [here](https://drive.google.com/file/d/1H6uSF-L3drCNzaMyKOzeUCbrH0FxGseg/view)
   - Move the downloaded file into /data/vectors/
3) python3 server.py
   - pip(3) install works for all libraries (flask_talisman, pandas, flask_sslify, scikit-learn==0.19)
   - pip3 install lib_name or python3 -m pip install lib_name
   - If required run using SSL by including one argument: 'python3 server.py SSL'
   
   


Coming soon:
  Docker container for easy install
