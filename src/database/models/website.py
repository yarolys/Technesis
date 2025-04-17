import pandas as pd
import httpx
from lxml import html
import re
from sqlalchemy import Float, String
from sqlalchemy.orm import Mapped, mapped_column
from src.database.connection import Base, async_session_maker


class Website(Base):
    __tablename__ = 'websites'

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    title: Mapped[str] = mapped_column(String, nullable=False)
    url: Mapped[str] = mapped_column(String, nullable=False, unique=True)
    xpath: Mapped[str] = mapped_column(String, nullable=False)
    price: Mapped[float | None] = mapped_column(Float, nullable=True)
    currency: Mapped[str | None] = mapped_column(String, nullable=True)  # Новый столбец для валюты

    def __repr__(self) -> str:
        return f"<Website {self.title}>"

    @classmethod
    async def dataframe(cls, df: pd.DataFrame):
        async with async_session_maker() as session:
            async with httpx.AsyncClient() as client:
                for _, row in df.iterrows():
                    price_value = None
                    currency = None
                    try:
                        response = await client.get(row['url'])
                        tree = html.fromstring(response.content)
                        price_raw = tree.xpath(row['xpath'])
                        if price_raw:
                            price_str = str(price_raw[0]).replace('\xa0', '').strip()
                            # Используем регулярные выражения для извлечения валюты и цены
                            match = re.match(r"([^\d]+)?(\d+(\.\d+)?)", price_str)
                            if match:
                                currency = match.group(1).strip() if match.group(1) else None
                                price_value = float(match.group(2))
                                
                            # Обрабатываем случаи, когда валюта не указана или некорректно извлечена
                            if currency is None:
                                currency = 'USD'  # если валюта не указана, предполагаем доллар
                    except Exception as e:
                        print(f"Ошибка при парсинге {row['url']}: {e}")

                    website = cls(
                        title=row['title'],
                        url=row['url'],
                        xpath=row['xpath'],
                        price=price_value,
                        currency=currency
                    )
                    session.add(website)
            await session.commit()