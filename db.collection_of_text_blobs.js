db.collection_of_text_blobs.aggregate(
    [
  {
    $search:
      /**
       * index: The name of the Search index.
       * text: Analyzed search, with required fields of query and path, the analyzed field(s) to search.
       * compound: Combines ops.
       * span: Find in text field regions.
       * exists: Test for presence of a field.
       * near: Find near number or date.
       * range: Find in numeric or date range.
       */
      {
        index: "vector_index",
        knnBeta: {
          vector: [0],
          path: "embedding",
          k: 1,
        },
      },
  },
]
)