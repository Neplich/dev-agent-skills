FROM nginx:1.27-alpine AS public
COPY .generated/public /usr/share/nginx/html
HEALTHCHECK CMD wget -qO- http://127.0.0.1/ || exit 1

FROM nginx:1.27-alpine AS internal
COPY .generated/internal /usr/share/nginx/html
COPY deploy/internal-auth.conf /etc/nginx/conf.d/default.conf
HEALTHCHECK CMD wget -qO- http://127.0.0.1/ || exit 1
