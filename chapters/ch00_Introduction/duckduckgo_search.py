import duckduckgo

for r in duckduckgo.query("Sausages").related:
    print(r.url + " - " + r.text)
