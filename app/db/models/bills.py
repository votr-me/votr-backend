from app.db.models.base import BaseModel
from sqlalchemy import Column, Integer, String, Text, DateTime, Boolean, func, ForeignKey, Index
from sqlalchemy.dialects.postgresql import BIGINT
from sqlalchemy.orm import relationship

class BillInfo(BaseModel):
    __tablename__ = "bill_info"
    __table_args__ = (
        Index('bill_info_congress_number_idx', 'congress', 'number'),
        Index('bill_info_latest_action_date_idx', 'latest_action_date'),  
        {'schema': 'raw'}
    )
    id = Column(String, primary_key=True)  
    congress = Column(BIGINT)  # Use BIGINT for larger range
    latest_action_date = Column(DateTime(timezone=True), nullable=True)  # Standardize timezone
    latest_action_text = Column(Text, nullable=True)  # Allow nulls
    number = Column(String)
    origin_chamber = Column(String)
    origin_chamber_code = Column(String) 
    title = Column(Text) 
    type = Column(String)
    update_date = Column(DateTime(timezone=True), nullable=True)  # Standardize timezone
    update_date_including_text = Column(Text, nullable=True)  # Allow nulls
    url = Column(String, nullable=True)
    latest_action_time = Column(DateTime(timezone=True), nullable=True)  # Standardize timezone
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    sponsors = relationship("BillSponsor", back_populates="bill")
    related_bills = relationship(
        "BillInfo", 
        secondary="bill_related_bills",  # Assuming you have a join table
        primaryjoin="BillInfo.id==bill_related_bills.c.bill_id",
        secondaryjoin="BillInfo.id==bill_related_bills.c.related_bill_id",
        backref="related_to"
    )