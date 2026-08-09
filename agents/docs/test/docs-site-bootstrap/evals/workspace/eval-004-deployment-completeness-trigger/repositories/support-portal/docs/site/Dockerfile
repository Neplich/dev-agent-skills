FROM nginx:1.27-alpine AS public
COPY .generated/public /usr/share/nginx/html

FROM nginx:1.27-alpine AS internal
COPY .generated/internal /usr/share/nginx/html
