"""CLI entrypoint for a minimal video-script chain."""

import argparse

from dotenv import load_dotenv

from src.chains.sample_chain import build_script_chain


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate a short video script outline.")
    parser.add_argument("--topic", default="product launch", help="Video topic")
    parser.add_argument("--audience", default="general", help="Target audience")
    parser.add_argument("--length", default="60s", help="Video length")
    parser.add_argument("--model", default="gpt-4o-mini", help="OpenAI model")
    return parser.parse_args()


def main() -> None:
    load_dotenv()
    args = parse_args()
    chain = build_script_chain(model=args.model)
    result = chain.invoke(
        {"topic": args.topic, "audience": args.audience, "length": args.length}
    )
    print(result)


if __name__ == "__main__":
    main()
