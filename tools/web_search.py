from enum import Enum

from ddgs import DDGS

class WebSearchStatus(str, Enum):
    NO_RESULTS = "No results found."


WEB_SEARCH_TOOL = {
    "type": "function",
    "function": {
        "name": "web_search",
        "description": "Search the web for current information. Such as current news, weather, and other live and modern information. This is not intended for conversational history or general knowledge.",
        "parameters": {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": "Search query",
                }
            },
            "required": ["query"],
        },
    },
}


class WebSearch:
    def __init__(self, verbose: bool = False):
        self._verbose = verbose

    def search(self, query: str) -> str:
        """Search the web for current information."""
        results = DDGS().text(query, max_results=5)
        if self._verbose:
            print(f"[WebSearch] query={query!r} results={len(results) if results else 0}")
            if results:
                for r in results:
                    print(f"[WebSearch] {r['title']}: {r['body']}")
        if not results:
            return WebSearchStatus.NO_RESULTS.value
        return "\n".join(f"{r['title']}: {r['body']}" for r in results)
