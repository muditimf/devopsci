FROM centos
MAINTAINER mudit shah
RUN yum install httpd -y
COPY index.html /var/www/html/index.html
EXPOSE 80
ENTRYPOINT httpd -DFOREGROUND
