# live-location

My docker run command:

docker run -d --network traefik --restart always -v /root/location/www.google.com_cookies.txt:/www.google.com_cookies.txt -v /matrix/traefik-certs-dumper/dumped-certificates/api.chagai.website/certificate.crt:/certificate.crt -v /matrix/traefik-certs-dumper/dumped-certificates/api.chagai.website/privatekey.key:/privatekey.key --label-file /matrix/chagai-location/labels --name chagai-location -p 4400:4400 chagai/chagai-location:1.0.6