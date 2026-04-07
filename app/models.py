from sqlalchemy import Column, Integer, String, Text
from app.database import Base

class RopaRecord(Base):
    __tablename__ = "ropa_records"

    id = Column(Integer, primary_key=True, index=True)
    ropa_type = Column(String, index=True) # 'controller' หรือ 'processor'
    
    sequence_no = Column(String)
    activity_name = Column(String)
    purpose = Column(Text)
    collected_personal_data = Column(Text)
    data_subject_category = Column(String)
    data_type = Column(String)
    collection_format = Column(String)
    legal_basis = Column(String)

    recorder_info_name = Column(String)
    recorder_info_address = Column(Text)
    recorder_info_email = Column(String)
    recorder_info_phone = Column(String)

    controller_info = Column(Text)
    data_source_is_direct_from_subject = Column(String)
    minor_consent_under_10_years = Column(Text)
    minor_consent_between_10_to_20_years = Column(Text)
    disclosure_without_consent = Column(Text)
    dsar_rejection_record = Column(Text)

    processor_name = Column(String)
    controller_address = Column(Text)
    data_source_is_direct_from_controller = Column(String)
    data_source_indirect_source_detail = Column(Text)

    cross_border_transfer_is_transferred = Column(String)
    cross_border_transfer_is_intra_group = Column(String)
    cross_border_transfer_transfer_method = Column(String)
    cross_border_transfer_destination_standard = Column(String)
    cross_border_transfer_section_28_exception = Column(Text)

    retention_policy_storage_format = Column(String)
    retention_policy_storage_method = Column(String)
    retention_policy_retention_period = Column(String)
    retention_policy_access_rights_and_methods = Column(Text)
    retention_policy_destruction_method = Column(Text)

    security_measures_organizational_measure = Column(Text)
    security_measures_technical_measure = Column(Text)
    security_measures_physical_measure = Column(Text)
    security_measures_access_control = Column(Text)
    security_measures_user_responsibility = Column(Text)
    security_measures_audit_trail = Column(Text)