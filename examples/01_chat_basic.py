#!/usr/bin/env python3
"""01 — One chat completion through the proxy.

Sends a single user message to gemini-3-flash and prints the reply.
Defaults to a local proxy; override GOP_BASE_URL / GOP_API_KEY for
remote deployments.
"""

import os
import sys

from openai import OpenAI

client = OpenAI(
    base_url=os.getenv("GOP_BASE_URL", "http://localhost:4982/openai/v1"),
    api_key=os.getenv("GOP_API_KEY", "not-verified"),
)

resp = client.chat.completions.create(
    model="gemini-3-flash",
    messages=[{"role": "user", "content": "how are u man reply in three sentence"}],
    temperature=0.7,
)

content = resp.choices[0].message.content
print(content)
