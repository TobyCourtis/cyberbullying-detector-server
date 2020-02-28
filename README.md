# cyberbullying-detector-server
Server component of the 'Cyberbullying Detector'

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
  Docker Container for easy install
