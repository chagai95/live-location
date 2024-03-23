# live-location

My docker run command:
docker run -d --network traefik --restart always -v /root/location/www.google.com_cookies.txt:/www.google.com_cookies.txt -v /matrix/traefik-certs-dumper/dumped-certificates/api.chagai.website/certificate.crt:/certificate.crt -v /matrix/traefik-certs-dumper/dumped-certificates/api.chagai.website/privatekey.key:/privatekey.key -v /matrix/chagai-location/config/config.toml:/config/config.toml --env-file /matrix/chagai-location/env --label-file /matrix/chagai-location/labels --name chagai-location -p 8080:4400 chagai/chagai-location:1.0.5