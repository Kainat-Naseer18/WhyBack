from datetime import datetime
from decimal import Decimal

from sqlalchemy import DateTime, ForeignKey, Integer, Numeric, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from backend.database import Base


class ReturnRecord(Base):
    __tablename__ = "returns"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    product_id: Mapped[int] = mapped_column(
        ForeignKey("products.id"),
        nullable=False
    )

    reason: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    customer_comment: Mapped[str | None] = mapped_column(
        Text,
        nullable=True
    )

    refund_amount: Mapped[Decimal] = mapped_column(
        Numeric(10, 2),
        nullable=False
    )

    return_date: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False
    )