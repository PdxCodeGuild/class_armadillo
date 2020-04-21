
# Deployment

## Hosting Services


- [PythonAnywhere](https://www.pythonanywhere.com/)
- [Heroku](https://devcenter.heroku.com/articles/deploying-python)
- [WebFaction](https://www.webfaction.com/)
- [NearlyFreeSpeech.net](https://www.nearlyfreespeech.net/)
- [Digital Ocean](https://www.digitalocean.com/)
- [Amazon Web Services (AWS)](https://aws.amazon.com/)
- [Microsoft Azure](https://azure.microsoft.com/en-us/)


## SaaS vs PaaS vs IaaS

|    | description | examples |
|--- |---          |---       |
| SaaS | Software as a Service: they provide nearly everything through an interface of their web application | Wordpress, Squarespace |
| PaaS | Platform as a Service:  they provide the software and hardware, you copy files over and configure | PythonAnywhere, NearlyFreeSpeech, Windows Azure, AWS |
| IaaS | Infrastructure as a Service: they provide the hardware, you install software | Digital Ocean, AWS |
| Self-hosted | You manage all the software and hardware |    |


[read more](https://www.bmc.com/blogs/saas-vs-paas-vs-iaas-whats-the-difference-and-how-to-choose/)



## Domain Names

Most hosting services will give your website a default domain name, but if you want something custom, you'll have to rent it from a domain registrar. You can then add a DNS record to associate it with your server's IP address. You can read more about domains on the [MDN](https://developer.mozilla.org/en-US/docs/Learn/Common_questions/What_is_a_domain_name).

To use a custom domain name, you have to register it with a domain registrar. Some hosting sites are also domain registrars, some are not.

- [Google Domains](https://domains.google/)
- [Hover](https://www.hover.com/)
- [GoDaddy](https://www.godaddy.com/)

## HTTPS

To allow your site to use HTTP, you must install an SSL Certificate on your server. SSL certificates can be purchased from a Commercial Certificate Authority, created with Let's Encrypt, or self-signed.

## Deploying Django with PythonAnywhere

Python [tutorial](https://help.pythonanywhere.com/pages/DeployExistingDjangoProject) and [video](https://www.youtube.com/watch?v=Y4c4ickks2A). If your project uses static files, check out [this document](https://help.pythonanywhere.com/pages/DjangoStaticFiles).


How to print to the error log on pythonanywhere

```python
import sys
print('check the error log', file=sys.stderr)
```

Find more info about virtual environments [here](https://github.com/PdxCodeGuild/class_honeybadger/blob/master/1%20Python/docs/Virtual%20Environments.md)

Deploying with Django channels is [more complicated](https://channels.readthedocs.io/en/latest/deploying.html)

