FROM caddy:alpine
WORKDIR /app
COPY dist ./dist
COPY Caddyfile .
CMD ["caddy", "run", "--config", "/app/Caddyfile", "--adapter", "caddyfile"]
