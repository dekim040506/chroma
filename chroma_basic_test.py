import chromadb

# 1. Chroma 데이터를 로컬 폴더에 저장하는 클라이언트 생성
# ./chroma_db 폴더가 자동으로 생성됩니다.
client = chromadb.PersistentClient(path="./chroma_db")

# 2. Collection 생성 또는 가져오기
# Collection은 문서들을 담는 저장 공간입니다.
collection = client.get_or_create_collection(name="my_first_collection")

# 3. 테스트 문서 저장
collection.add(
    documents=[
        "Chroma는 RAG에서 문서를 벡터로 저장하고 검색하는 데 사용된다.",
        "Giskard는 LLM 모델의 취약점과 품질을 진단하는 데 사용할 수 있다.",
        "RAGAS는 RAG 시스템의 답변 품질을 평가하는 도구이다."
    ],
    metadatas=[
        {"source": "chroma_intro"},
        {"source": "giskard_intro"},
        {"source": "ragas_intro"}
    ],
    ids=[
        "doc1",
        "doc2",
        "doc3"
    ]
)

print("저장 완료")

# 4. 저장된 문서 개수 확인
count = collection.count()
print("저장된 문서 개수:", count)

# 5. 질문과 의미적으로 가까운 문서 검색
results = collection.query(
    query_texts=["RAG에서 문서를 저장하고 검색하는 도구는 무엇인가?"],
    n_results=2
)

print("\n검색 결과:")
print(results)



# {'ids': 
# [['doc3', 'doc1']], 'embeddings': None, 'documents': 
# [['RAGAS는 RAG 시스템의 답변 품질을 평가하는 도구이다.', 'Chroma는 RAG에서 문서를 벡터로 저장하고 검색하는 데 사용된다.']], 'uris': 
# None, 

# 'included': 
# ['metadatas', 'documents', 'distances'], 

# 'data': None, 

# 'metadatas': 
# [[{'source': 'ragas_intro'}, {'source': 'chroma_intro'}]], 
# 'distances': [[0.31285181641578674, 0.7401019930839539]]}