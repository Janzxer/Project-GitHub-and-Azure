for limit_doc in limit(documents):
    response = requests.post(sentiment_url, headers = headers, json={"documents": limit_doc})
    
    response.raise_for_status()
    data = response.json()

    for t in data.get("documents", []):
        sentiment_results[t["id"]] = t["sentiment"]

for i, article in enumerate(parsed_articles, start=1):
    article["title_sentiment"] = sentiment_results.get(str(i), "unknown")