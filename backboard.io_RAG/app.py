import asyncio
from services.backboard_service import BackboardService
from utils.helpers import print_divider


async def main():
    service = BackboardService()

    #Create assistant
    assistant = await service.create_assistant()
    print("Assistant created:", assistant.assistant_id)

    print_divider()

    # Upload document
    document = await service.upload_and_index_document(
        assistant.assistant_id,
        "my_document.pdf"
    )

    print_divider()

    # Ask question
    await service.ask_question(
        assistant.assistant_id,
        "What are the key points in the uploaded document?"
    )


if __name__ == "__main__":
    asyncio.run(main())