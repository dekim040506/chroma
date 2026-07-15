import streamlit as st
import chromadb
import pandas as pd

DB_PATH = "/Users/kimdong-eul/myprojects/chroma/chroma_db"

st.set_page_config(
    page_title="Chroma DB Viewer",
    layout="wide"
)

st.title("Chroma DB Viewer")

client = chromadb.PersistentClient(path=DB_PATH)

collections = client.list_collections()
collection_names = [c.name for c in collections]

st.subheader("Collections")
st.write(collection_names)

selected = st.selectbox(
    "컬렉션 선택",
    collection_names
)

if selected:
    collection = client.get_collection(selected)
    st.write("문서 개수:", collection.count())

    result = collection.get()

    df = pd.DataFrame({
        "id": result["ids"],
        "document": result["documents"],
        "metadata": result["metadatas"]
    })

    st.subheader("Stored Documents")
    st.dataframe(df, use_container_width=True)

    st.subheader("Semantic Search")

    query = st.text_input("검색어를 입력하세요")

    n_results = st.slider(
        "검색 결과 개수",
        min_value=1,
        max_value=10,
        value=3
    )

    if query:
        search_result = collection.query(
            query_texts=[query],
            n_results=n_results
        )

        search_df = pd.DataFrame({
            "id": search_result["ids"][0],
            "document": search_result["documents"][0],
            "distance": search_result["distances"][0]
        })

        st.subheader("Search Results")
        st.dataframe(search_df, use_container_width=True)

        # streamlit run 21_chroma_viewer.py
