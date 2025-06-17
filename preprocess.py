import json
import re
from llm_helper import llm
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException

def clean_text(text: str) -> str:
    """
    Strip out any lone surrogate code points (U+D800–DFFF).
    """
    return re.sub(r'[\ud800-\udfff]', '', text)

def process_posts(raw_file_path: str, processed_file_path: str):
    # Load raw posts
    with open(raw_file_path, encoding='utf-8') as file:
        posts = json.load(file)

    enriched_posts = []
    for post in posts:
        # 1) Clean the original text in-place to strip surrogates
        raw_text = post.get('text', '')
        cleaned_text = clean_text(raw_text)
        post['text'] = cleaned_text

        # 2) Extract metadata from the cleaned text
        metadata = extract_metadata(post_text=cleaned_text)

        # 3) Merge and collect
        post_with_metadata = {**post, **metadata}
        enriched_posts.append(post_with_metadata)

    # Build unified tag mapping
    unified_tags = get_unified_tags(enriched_posts)

    # Apply unified tags
    for post in enriched_posts:
        current = post.get('tags', [])
        post['tags'] = [unified_tags.get(tag, tag) for tag in current]

    # Write out processed posts (all text is now safe)
    with open(processed_file_path, mode="w", encoding="utf-8") as outfile:
        json.dump(enriched_posts, outfile, indent=4, ensure_ascii=False)

def extract_metadata(post_text: str):
    template = '''
You are given a LinkedIn post. You need to extract number of lines, language of the post and tags.
1. Return a valid JSON. No preamble.
2. JSON object should have exactly three keys: line_count, language and tags.
3. tags is an array of text tags. Extract maximum two tags.
4. Language should be English or Hinglish (Hinglish means Hindi + English).

Here is the actual post on which you need to perform this task:
{post}
'''
    pt = PromptTemplate.from_template(template)
    chain = pt | llm

    # We already cleaned post_text above
    response = chain.invoke(input={"post": post_text})

    try:
        parser = JsonOutputParser()
        return parser.parse(response.content)
    except OutputParserException:
        raise OutputParserException("Context too big. Unable to parse metadata.")

def get_unified_tags(posts_with_metadata):
    unique = set()
    for post in posts_with_metadata:
        unique.update(post.get('tags', []))

    tags_str = ",".join(unique)
    template = '''
I will give you a list of tags. You need to unify tags with the following requirements:
1. Merge related tags into a single canonical form.
2. Title-case each unified tag.
3. Output a JSON object mapping each original tag to its unified tag.

Here is the list of tags:
{tags}
'''
    pt = PromptTemplate.from_template(template)
    chain = pt | llm

    response = chain.invoke(input={"tags": tags_str})

    try:
        parser = JsonOutputParser()
        return parser.parse(response.content)
    except OutputParserException:
        raise OutputParserException("Context too big. Unable to parse tag mappings.")

if __name__ == "__main__":
    process_posts("data/raw_posts.json", "data/processed_posts.json")
