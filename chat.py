#!/usr/bin/env python3
"""Interactive test console for Gemini WebAPI Proxy.

Keeps the connection open for fast responses. Type your prompt and press Enter.
"""

import sys
from openai import OpenAI

def main():
    print("=" * 60)
    print("🤖 Gemini WebAPI Proxy — Interactive Chat Tester")
    print("Endpoint : http://localhost:4982/openai/v1")
    print("Model    : gemini-flash-lite (Fastest)")
    print("Type 'exit' or 'quit' to close.")
    print("=" * 60)

    client = OpenAI(
        base_url="http://localhost:4982/openai/v1",
        api_key="not-verified",
    )

    while True:
        try:
            prompt = input("\nYou > ").strip()
            if not prompt:
                continue
            if prompt.lower() in ("exit", "quit", "q"):
                print("Goodbye!")
                break

            print("Thinking...", end="\r", flush=True)

            response = client.chat.completions.create(
                model="gemini-flash-lite",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.7,
            )

            reply = response.choices[0].message.content
            print(f"Gemini > {reply}")

        except KeyboardInterrupt:
            print("\nExiting...")
            break
        except Exception as err:
            print(f"\n[Error] {err}")

if __name__ == "__main__":
    main()
