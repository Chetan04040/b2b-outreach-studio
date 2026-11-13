import re
from typing import Dict, Optional
import requests
from bs4 import BeautifulSoup


class WebScraper:
    """Safely extracts business context and metadata from a target company URL."""

    HEADERS = {
        "User-Agent": (
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
            "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        ),
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
    }

    @classmethod
    def scrape_url(cls, url: str, timeout: int = 10) -> Dict[str, Optional[str]]:
        """Fetch URL content and extract title, description, and core textual copy."""
        if not url.startswith(("http://", "https://")):
            url = f"https://{url}"

        try:
            response = requests.get(url, headers=cls.HEADERS, timeout=timeout)
            response.raise_for_status()

            soup = BeautifulSoup(response.text, "html.parser")

            # Remove noisy tags
            for tag in soup(["script", "style", "noscript", "svg", "header", "footer", "nav"]):
                tag.extract()

            title = soup.title.string.strip() if soup.title and soup.title.string else ""

            # Extract meta description
            desc_tag = soup.find("meta", attrs={"name": "description"}) or soup.find("meta", attrs={"property": "og:description"})
            description = desc_tag["content"].strip() if desc_tag and "content" in desc_tag.attrs else ""

            # Extract headers and body paragraphs
            headings = [h.get_text(strip=True) for h in soup.find_all(["h1", "h2", "h3"])[:8]]
            paragraphs = [p.get_text(strip=True) for p in soup.find_all("p") if len(p.get_text(strip=True)) > 40][:10]

            combined_text = "\n".join(headings + paragraphs)
            cleaned_text = re.sub(r"\s+", " ", combined_text).strip()[:3500]

            return {
                "url": url,
                "title": title,
                "meta_description": description,
                "content_snippet": cleaned_text,
                "success": True,
                "error": None,
            }

        except Exception as exc:
            return {
                "url": url,
                "title": "",
                "meta_description": "",
                "content_snippet": "",
                "success": False,
                "error": str(exc),
            }
