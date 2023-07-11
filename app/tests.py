#!/usr/bin/env python
import unittest
from unittest.mock import MagicMock, patch
from unittest import skip

from api.slack.routes import send_to_slack
from api.slack.routes import SlackMessageIn


class SlackMessageTest(unittest.TestCase):
    @patch("slack.WebClient")
    def test_send_to_slack_with_text_only(self, mock_web_client):
        payload = {
            "channel": "#test-channel",
            "mentions": ["@test-user"],
            "text": "Hello, World!",
        }

        mock_chat_post_message = MagicMock(return_value={"ok": True})
        mock_web_client.return_value.chat_postMessage = mock_chat_post_message

        response = send_to_slack(SlackMessageIn(**payload))
        self.assertTrue(response["result"])
        mock_chat_post_message.assert_called_once_with(
            channel="#test-channel", text="Hello, World!"
        )

    @patch("slack.WebClient")
    def test_send_to_slack_with_blocks(self, mock_web_client):
        payload = {
            "channel": "#test-channel",
            "blocks": [
                {
                    "type": "section",
                    "text": {"type": "mrkdwn", "text": "Hello, Assistant!"},
                }
            ],
        }
        mock_chat_post_message = MagicMock(return_value={"ok": True})
        mock_web_client.return_value.chat_postMessage = mock_chat_post_message

        response = send_to_slack(SlackMessageIn(**payload))

        self.assertTrue(response["result"])
        mock_chat_post_message.assert_called_once_with(
            channel="#test-channel",
            blocks=[
                {
                    "type": "section",
                    "text": {"type": "mrkdwn", "text": "Hello, Assistant!"},
                }
            ],
        )


if __name__ == "__main__":
    unittest.main()
