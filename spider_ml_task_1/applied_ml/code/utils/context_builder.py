def build_context(docs):

    context = []

    for doc in docs:

        source = doc.metadata["source"]

        context.append(
            f"[Source: {source}]\n{doc.page_content}"
        )

    return "\n\n".join(context)