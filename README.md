# cyberbullying-detector-server
Server component of the 'Cyberbullying Detector'

How to run the Server:

1) Aquire SSL Certificates if requiring https
   - Label 'cert.pem' and 'key.pem' then transfer into 'ssl_certificates' directory
2) python3 server.py
   - pip(3) install works for all libraries (flask_talisman, pandas, flask_sslify, scikit-learn==0.19)
   - pip3 install lib_name or python3 -m pip install lib_name
   - If required run using SSL by including one argument: 'python3 server.py SSL'
   
   
   

Coming soon:
  Docker Container
