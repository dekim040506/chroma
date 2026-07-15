import chromadb
import pandas as pd
import json
from datetime import datetime

DB_PATH = "/Users/kimdong-eul/myprojects/chroma/chroma_db"
COLLECTION_NAME = "my_first_collection"

client = chromadb.PersistentClient(path=DB_PATH)
collection = client.get_collection(COLLECTION_NAME)

result = collection.get(
    include=["documents", "metadatas"]
)

rows = []

for i in range(len(result["ids"])):
    rows.append({
        "ID": result["ids"][i],
        "Document": result["documents"][i],
        "Metadata": json.dumps(result["metadatas"][i], ensure_ascii=False)
    })

df = pd.DataFrame(rows)

now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
file_time = datetime.now().strftime("%Y%m%d_%H%M%S")

html_table = df.to_html(
    index=False,
    escape=True,
    border=0
)

html = f"""
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <title>Chroma DB Export Report</title>
    <style>
        body {{
            font-family: Arial, Apple SD Gothic Neo, sans-serif;
            margin: 40px;
            background-color: #f7f7f7;
            color: #222;
        }}

        h1 {{
            color: #333;
        }}

        .summary {{
            background-color: white;
            padding: 16px;
            border-radius: 8px;
            margin-bottom: 24px;
            border: 1px solid #ddd;
        }}

        table {{
            width: 100%;
            border-collapse: collapse;
            background-color: white;
        }}

        th {{
            background-color: #333;
            color: white;
            padding: 10px;
            text-align: left;
        }}

        td {{
            border: 1px solid #ddd;
            padding: 10px;
            vertical-align: top;
        }}

        tr:nth-child(even) {{
            background-color: #f2f2f2;
        }}
    </style>
</head>
<body>

    <h1>Chroma DB Export Report</h1>

    <div class="summary">
        <p><strong>DB Path:</strong> {DB_PATH}</p>
        <p><strong>Collection:</strong> {COLLECTION_NAME}</p>
        <p><strong>Document Count:</strong> {collection.count()}</p>
        <p><strong>Generated At:</strong> {now}</p>
    </div>

    {html_table}

</body>
</html>
"""

output_file = f"chroma_export_{COLLECTION_NAME}_{file_time}.html"

with open(output_file, "w", encoding="utf-8") as f:
    f.write(html)

print("HTML 파일 생성 완료:", output_file)