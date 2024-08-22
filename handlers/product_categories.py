from aiogram import types, Router
from aiogram.types import FSInputFile


router = Router()


@router.message(lambda message: message.text == "Сумки")
async def show_bags_catalog(message: types.Message):
    bags = [
        {
            "photo_path": "images/bags/2024-08-21 16.42.06.jpg",
            "caption": (
                "Сумка \"Tommy Brown\"\n"
                "Размер: one size\n"
                "Артикул: 003TbV\n"
                "✅ В наличии"
            )
        },
    ]
    for bag in bags:
        await message.answer_photo(photo=FSInputFile(bag['photo_path']), caption=bag['caption'])


@router.message(lambda message: message.text == "Платья и сарафаны")
async def show_bags_catalog(message: types.Message):
    dress = [
        {
            "photo_path": "images/dress/2024-08-22 09.38.01.jpg",
            "caption": (
                "Сарафан \"Mini milk\"\n"
                "Размер: 42-44, 46-48\n"
                "Артикул: :001dMM\n"
                "🔜 Доступен к предзаказу до 01.09.2024"
            )
        }
    ]

    for dres in dress:
        await message.answer_photo(photo=FSInputFile(dres['photo_path']), caption=dres["caption"])

