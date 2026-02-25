"""Tools for executing REST API calls based on specifications."""

from __future__ import annotations

import json
from typing import Any, Dict, Optional
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode, urlsplit, urlunsplit
from urllib.request import Request, urlopen


def get_request(
	url: str,
	params: Optional[Dict[str, Any]] = None,
	headers: Optional[Dict[str, str]] = None,
	timeout_seconds: int = 15,
) -> Dict[str, Any]:
	"""Perform an HTTP GET call and return status, headers, and parsed body."""
	params = params or {}
	headers = headers or {}

	split_url = urlsplit(url)
	query = split_url.query
	if params:
		query = "&".join(filter(None, [query, urlencode(params, doseq=True)]))

	full_url = urlunsplit(
		(split_url.scheme, split_url.netloc, split_url.path, query, split_url.fragment)
	)

	request = Request(full_url, headers=headers, method="GET")

	try:
		with urlopen(request, timeout=timeout_seconds) as response:
			content_type = response.headers.get("Content-Type", "")
			raw_body = response.read()
			body_text = raw_body.decode("utf-8", errors="replace")
			if "application/json" in content_type:
				body: Any = json.loads(body_text) if body_text else None
			else:
				body = body_text

			return {
				"url": full_url,
				"status": response.status,
				"headers": dict(response.headers),
				"body": body,
			}
	except HTTPError as exc:
		error_body = exc.read().decode("utf-8", errors="replace") if exc.fp else ""
		return {
			"url": full_url,
			"status": exc.code,
			"headers": dict(exc.headers) if exc.headers else {},
			"body": error_body,
			"error": str(exc),
		}
	except URLError as exc:
		return {
			"url": full_url,
			"status": None,
			"headers": {},
			"body": None,
			"error": str(exc),
		}

