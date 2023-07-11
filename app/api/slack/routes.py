import logging
from typing import Any, List, Optional

import slack
from cachetools.func import ttl_cache
from fastapi import APIRouter, Body, HTTPException
from pydantic import BaseModel
from utils import get_logger
from config import settings

logger = get_logger("app")


class SlackMessageIn(BaseModel):
    channel: str
    mentions: list = None
    blocks: Optional[List[dict]] = None
    text: str = None


router = APIRouter()


@ttl_cache(ttl=5 * 60 * 60)  # cache for 5 hours
def get_member_list():
    client = slack.WebClient(token=settings.SLACK_BOT_TOKEN)
    try:
        response = client.users_list()
        return response["members"]
    except slack.errors.SlackApiError as e:
        logger.error(f"Error getting members list: {e}")
        return []


def get_user_id_by_username(username: str, member_list: list = None):
    for member in member_list:
        if (
            "profile" in member
            and member["profile"]["display_name"]
            and "@" + member["profile"]["display_name"].lower() == username.lower()
        ):
            return member["id"]
    return None


@router.post("")
def send_to_slack(
    payload: SlackMessageIn = Body(
        None,
        description="Send a message to slack",
        examples={
            "Send plaintext message": {
                "value": {
                    "channel": "#test-channel",
                    "mentions": ["@test-user"],
                    "text": "Hello, World!",
                },
            },
            "Send blocks": {
                "value": {
                    "channel": "#test-channel",
                    "blocks": [
                        {
                            "type": "section",
                            "text": {
                                "type": "mrkdwn",
                                "text": "Hello, Assistant to the Regional Manager Dwight! *Michael Scott* wants to know where you'd like to take the Paper Company investors to dinner tonight.\n\n *Please select a restaurant:*",
                            },
                        },
                        {"type": "divider"},
                        {
                            "type": "section",
                            "text": {
                                "type": "mrkdwn",
                                "text": "*Farmhouse Thai Cuisine*\n:star::star::star::star: 1528 reviews\n They do have some vegan options, like the roti and curry, plus they have a ton of salad stuff and noodles can be ordered without meat!! They have something for everyone here",
                            },
                            "accessory": {
                                "type": "image",
                                "image_url": "https://s3-media3.fl.yelpcdn.com/bphoto/c7ed05m9lC2EmA3Aruue7A/o.jpg",
                                "alt_text": "alt text for image",
                            },
                        },
                        {"type": "divider"},
                        {
                            "type": "section",
                            "text": {
                                "type": "mrkdwn",
                                "text": "This is a mrkdwn section block :ghost: *this is bold*, and ~this is crossed out~, and <https://google.com|this is a link>",
                            },
                        },
                    ],
                },
            },
        },
    )
) -> Any:
    """
    Send a message to a slack workspace.
    Messages are sent as "blocks", which are a collection of components that can be combined to create visually rich
    and compellingly interactive messages.
    Go to [slack block-kit builder docs](https://app.slack.com/block-kit-builder) for more examples.

    """
    channel = payload.channel
    mentions = payload.mentions
    text = payload.text
    blocks = payload.blocks
    client = slack.WebClient(token=settings.SLACK_BOT_TOKEN)

    if not blocks and not text:
        raise HTTPException(
            status_code=400, detail="Either blocks or text must be provided."
        )
    if mentions and text:
        member_list = get_member_list()
        user_ids = (
            [get_user_id_by_username(username, member_list) for username in mentions]
            if mentions
            else []
        )
        if any(user_ids):
            mentions_text = " ".join(f"<@{user_id}>" for user_id in user_ids if user_id)
            text = f"{mentions_text} {text}"
    if text and not blocks:
        result = client.chat_postMessage(channel=channel, text=text)
    else:
        result = client.chat_postMessage(channel=channel, blocks=blocks)
    return {"result": result.get("ok")}
