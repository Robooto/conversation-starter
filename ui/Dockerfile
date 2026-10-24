FROM node:22.23.4-bookworm-slim AS build-stage
RUN apt-get update \
    && apt-get install -y --no-install-recommends libbrotli1 \
    && dpkg --compare-versions "$(dpkg-query -W -f='${Version}' libbrotli1)" ge '1.0.9-2+deb12u1' \
    && rm -rf /var/lib/apt/lists/*
WORKDIR /app
COPY package*.json ./
RUN npm ci --legacy-peer-deps --no-audit --no-fund
COPY ./ .
# Webpack 4 uses legacy hashes. Limit this compatibility switch to the build;
# Node and its options are not shipped in the Nginx runtime image.
RUN NODE_OPTIONS=--openssl-legacy-provider npm run dev

FROM nginx:stable-trixie AS production-stage
LABEL org.opencontainers.image.source="https://github.com/Robooto/conversation-starter"
RUN apt-get update \
    && apt-get install -y --no-install-recommends libbrotli1 \
    && dpkg --compare-versions "$(dpkg-query -W -f='${Version}' libbrotli1)" ge '1.1.0-2+deb13u1' \
    && rm -rf /var/lib/apt/lists/*
RUN mkdir /app
COPY --from=build-stage /app/dist /app
COPY nginx.conf /etc/nginx/nginx.conf
