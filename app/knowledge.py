import re
from pathlib import Path

KNOWLEDGE_FILE = Path(__file__).resolve().parent.parent / "knowledge" / "faq.md"
STOP_WORDS = {
    "a", "an", "and", "are", "as", "at", "be", "by", "can", "do", "for",
    "from", "how", "i", "in", "is", "it", "me", "my", "of", "on", "or",
    "our", "please", "the", "this", "to", "we", "what", "when", "where",
    "which", "with", "you", "your",
}


def _tokens(text: str) -> set[str]:
    return {word for word in re.findall(r"[a-z0-9]{2,}", text.lower()) if word not in STOP_WORDS}


def load_sections() -> list[dict[str, str]]:
    if not KNOWLEDGE_FILE.exists():
        return []
    text = KNOWLEDGE_FILE.read_text(encoding="utf-8")
    text = re.sub(r"<!--.*?-->", "", text, flags=re.DOTALL)
    headings = list(re.finditer(r"(?m)^##\s+(.+?)\s*$", text))
    sections = []
    for index, heading in enumerate(headings):
        end = headings[index + 1].start() if index + 1 < len(headings) else len(text)
        content = text[heading.end():end].strip()
        if content:
            sections.append({"title": heading.group(1).strip(), "content": content})
    return sections


def find_relevant_sections(query: str, limit: int = 3) -> list[dict[str, str]]:
    query_tokens = _tokens(query)
    if not query_tokens:
        return []
    ranked = []
    for section in load_sections():
        section_tokens = _tokens(section["title"] + " " + section["content"])
        score = len(query_tokens & section_tokens)
        if score:
            ranked.append((score, section))
    ranked.sort(key=lambda item: item[0], reverse=True)
    return [section for _, section in ranked[:limit]]