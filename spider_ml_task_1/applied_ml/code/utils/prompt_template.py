def build_prompt(context, question):

    return f"""
Context:

{context}

Question:
{question}

Answer:
"""