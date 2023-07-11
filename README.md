# Slackbot Service

## Purpose
This service will live in the cluster and any other service can POST messages 
to be delivered to your company slack.

## Getting started

1. clone repo 
2. Add a `.env` file to project root with `SLACK_BOT_TOKEN="<secret>"`
3. run `docker compose up -d`
4. go to http://localhost:7171/docs to learn how to use.

## Slack app

Go here to configure: [https://api.slack.com/apps/A054K9Z9JUD/general](https://api.slack.com/apps/A054K9Z9JUD/general)
