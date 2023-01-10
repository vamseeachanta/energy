## Introduction
The document describes the programming principles to be the followed for typical programming projects:

## Summary

Static website:
https://firebase.google.com/pricing



### Heroku

https://www.heroku.com/pricing (USD 7 to include SSL verification)
https://devcenter.heroku.com/articles/custom-domains

Heroku commands for redeploy a git repo: Currently doing a manual deploy

Domain Name: *.hairbylizbellaire.com
DNS Target: metric-romaine-grpt3rxvnsaz30chctspaqql.herokudns.com

#### SSL Cert

**Heroku**
- I upgraded the dyno type - did not work. 
- Then deleted the cert assignment and started from scratch and it worked. 
- The cert created by me is still shown to be given be Amazon for some reason : good.

To show SSL cert in GoDaddy or domain level. Follow steps in links below
- 

https://help.heroku.com/J2R1S4T8/can-heroku-force-an-application-to-use-ssl-tls
https://devcenter.heroku.com/articles/preparing-a-java-web-app-for-production-on-heroku
https://community.godaddy.com/s/question/0D53t00006VmZF0CAN/heroku-custom-domain-acm-ssl-godaddy-not-secure
https://serverfault.com/questions/1000006/when-i-type-www-agavepv-com-into-the-browser-why-does-it-show-up-as-not-secure

## SSL Certificate

https://www.godaddy.com/help/set-up-my-managed-ssl-certificate-32212

https://devcenter.heroku.com/articles/ssl

<code>
heroku domains:update www.hairbylizbellaire.com --cert selfsigned --app hairbyliz

Updating www.hairbylizbellaire.com to use selfsigned certificate... done
 »   Error: Couldn't find that domain name.
 »
 »   Error ID: not_found
</code>

selfsigned certificates can be obtained using programming. Eg using pythong
py\utilities\generate_ssl.py

free ca certificates can be obtained using below:
https://letsencrypt.org/getting-started/

Steps:
For looking at the domain particulars
https://lookup.icann.org/en/lookup

For generating a csr:
https://blog.hubspot.com/website/best-free-ssl-certificate-sources
https://www.digicert.com/easy-csr/openssl.htm
https://decoder.link/csr_generator


### Troubleshooting Tips

Open command prompt:

**GoDaddy**

<code>
ping hairbylizbellaire.com

    Pinging hairbylizbellaire.com [34.102.136.180] with 32 bytes of data:
    Reply from 34.102.136.180: bytes=32 time=14ms TTL=56
    Reply from 34.102.136.180: bytes=32 time=15ms TTL=56
</code>


<code>
nslookup hairbylizbellaire.com

    Server:  UnKnown
    Address:  2601:2c0:8f00:ef:9610:3eff:fe0d:5537

    Non-authoritative answer:
    Name:    hairbylizbellaire.com
    Address:  34.102.136.180
</code>

**Heroku**


<code>
ping hairbyliz.heroku.com
    Not working
</code>


<code>
nslookup hairbyliz.heroku.com
    Server:  UnKnown
    Address:  2601:2c0:8f00:ef:9610:3eff:fe0d:5537
</code>

<code>
telnet hairbyliz.heroku.com:8080
    Connecting To hairbyliz.heroku.com:8080...Could not open connection to the host, on port 23: Connect failed
</code>

it\web_hosting\heroku_ssl_setup.png
