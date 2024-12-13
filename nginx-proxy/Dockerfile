FROM ubuntu:latest

RUN apt-get update && \
     apt install -y nginx

COPY default.conf /etc/nginx/sites-available/default
EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]