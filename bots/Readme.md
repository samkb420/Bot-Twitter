## python bot for marketing

### Build command for image

```shell
docker build . -t fav-retweet-bot
```



#### Test the docker image by passing this:-

```shell
docker run -it -e CONSUMER_KEY="uDRNy31oWfoiKV9AvPoNavy0I" \
 -e CONSUMER_SECRET="lnAL5VAgZLWNspQVpd3X6tEo47PRCmsPEwuxpvLCLSR08DMa4O" \
 -e ACCESS_TOKEN="622518593-j7gWSqzQO31ju7Bf7idB47NlZeSENsuADGU9B69I" \
 -e ACCESS_TOKEN_SECRET="iutFsxvP5IglRckJ1I1why6017xMNkzxqBID48Azw0GvT" \
 fav-retweet-bot
```

### preparing for deploy for our image:

```shell
docker image save fav-retweet-bot:latest -o fav-retweet-bot.tar
$ gzip fav-retweet-bot.tar
```