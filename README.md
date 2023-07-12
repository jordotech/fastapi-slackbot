# FastAPI + Slack + Docker

Dead simple docker image you can use to send messages from all your apps to your slack.

## Demo

#### 1. Join the sandbox slack workspace

I've created a sandbox slack workspace (`slackbot-sandbox-e0f8`) for anyone to test, click or copy/paste this invite link to join the workspace:
[https://join.slack.com/t/newworkspace-yfo6489/shared_invite/zt-1zctp22u8-biUNZJvgGPLFBraJRP8v2A](https://join.slack.com/t/newworkspace-yfo6489/shared_invite/zt-1zctp22u8-biUNZJvgGPLFBraJRP8v2A)

Then view the `#testing` channel: [https://app.slack.com/client/T05HDNQB99N/C05GSFEN2N8](https://app.slack.com/client/T05HDNQB99N/C05GSFEN2N8)

#### 2. Start the docker image with the provided token

(The token `xoxb-5591772383328-5565297345781-nJVVXl8frk6rV59yOHUkjyai` is available for testing purposes)


```shell
docker run --rm -e SLACK_BOT_TOKEN=xoxb-5591772383328-5565297345781-nJVVXl8frk6rV59yOHUkjyai --name slackbot -p 7171:80 jordotech/fastapi-slackbot:latest
```

#### 3. Send a notification

```
curl --location 'http://localhost:7171/send-message' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--data '{
  "channel": "#testing",
  "text": "Hello, World!"
}'
```

Your message should appear in the `#testing` channel in slack.


## Run Locally with Docker Compose
1. Clone this repo
2. Create a `.env` file in the project root with `SLACK_BOT_TOKEN=<your_token>`
3. Run `docker compose up -d`

Then open [http://localhost:7171/docs](http://localhost:7171/docs) to view the swagger and experiment sending messages.
