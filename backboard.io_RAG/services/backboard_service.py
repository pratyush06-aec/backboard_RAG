import asyncio
from backboard import BackboardClient
from utils.config import BACKBOARD_API_KEY


class BackboardService:
    def __init__(self):
        self.client = BackboardClient(api_key=BACKBOARD_API_KEY)

    async def create_assistant(self):
        return await self.client.create_assistant(
            name="Document Assistant",
            system_prompt="You are a helpful document analysis assistant"
        )

    async def upload_and_index_document(self, assistant_id, file_path):
        document = await self.client.upload_document_to_assistant(
            assistant_id,
            file_path
        )

        print("Waiting for document to be indexed...")

        while True:
            status = await self.client.get_document_status(document.document_id)

            if status.status == "indexed":
                print("Document indexed successfully!")
                return document

            elif status.status == "failed":
                raise Exception(f"Indexing failed: {status.status_message}")

            await asyncio.sleep(2)

    async def ask_question(self, assistant_id, question):
        thread = await self.client.create_thread(assistant_id)

        response = ""

        async for chunk in await self.client.add_message(
            thread_id=thread.thread_id,
            content=question,
            stream=True
        ):
            if chunk.get("type") == "content_streaming":
                c = chunk.get("content", "")
                if c:
                    print(c, end="", flush=True)
                    response += c

        print()
        return response