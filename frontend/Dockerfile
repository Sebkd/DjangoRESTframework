FROM nginx:1.21.6-alpine

COPY ./build ./var/www
COPY nginx.conf /etc/nginx/nginx.conf

# можно просто скопировать nginx как выше, можно стереть default и скопировать файл как показано ниже
# при наличии файла nginx.conf сам nginx не смотрит файл default.conf
#RUN rm /etc/nginx/conf.d/default.conf
#COPY nginx.conf /etc/nginx/conf.d
