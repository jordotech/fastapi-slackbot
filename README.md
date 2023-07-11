# FastAPI + Slack

Super simple docker image you can use to send messages from all your apps to your slack.

## Docker

You can pull and run the docker image, just supply your `SLACK_BOT_TOKEN` as an env var

## Run locally

```shell
docker run --rm -e SLACK_BOT_TOKEN=<your_token> --name slackbot -p 7171:80 jordotech/fastapi-slackbot:latest
```

## Local Docker Compose
1. Clone this repo
2. Create a `.env` file in the project root with `SLACK_BOT_TOKEN=<your_token>`
3. Run `docker compose up -d`

Then open [http://localhost:7171/docs](http://localhost:7171/docs) to view the swagger and experiment sending messages.
