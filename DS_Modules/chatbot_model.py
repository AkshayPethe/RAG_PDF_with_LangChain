from langchain_community.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain



def get_conversation_chain(vectorstore):
    llm = ChatOpenAI(openai_api_key="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",
                     model_name="gpt-3.5-turbo")

    memory = ConversationBufferMemory(
        memory_key='chat_history', return_messages=True)
    conversation_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vectorstore.as_retriever(),
        memory=memory
    )
    return conversation_chain
