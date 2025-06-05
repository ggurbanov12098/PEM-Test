# PEM-Test

```python
pip install sympy  
```

```bash
openssl rsa -pubin -in pubkey.pem -text -noout
```

Look for:  
Modulus: – this is your n (in hex)  
Exponent: – this is your e (usually small like 65537)  

Example output:
```bash
Modulus:
    00:c3:0d:1b:05:ba:6f...
Exponent: 65537 (0x10001)
```  

To get n as an integer:
```bash
openssl rsa -pubin -in pubkey.pem -modulus -noout
```

