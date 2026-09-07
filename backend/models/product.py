from decimal import Decimal

from sqlalchemy import ForeignKey, Integer, Numeric, String
from sqlalchemy.orm import Mapped, mapped_column

from backend.database import Base


class Product(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    business_id: Mapped[int] = mapped_column(
        ForeignKey("businesses.id"),
        nullable=False
    )

    sku: Mapped[str] = mapped_column(String(100), nullable=False)

    name: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    category: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True
    )

    price: Mapped[Decimal] = mapped_column(
        Numeric(10, 2),
        nullable=False
    )