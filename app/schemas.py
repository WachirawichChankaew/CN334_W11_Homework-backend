from pydantic import BaseModel
from typing import Optional

class RopaSchema(BaseModel):
    ropa_type: str
    sequence_no: Optional[str] = None
    activity_name: Optional[str] = None
    purpose: Optional[str] = None
    collected_personal_data: Optional[str] = None
    data_subject_category: Optional[str] = None
    data_type: Optional[str] = None
    collection_format: Optional[str] = None
    legal_basis: Optional[str] = None

    recorder_info_name: Optional[str] = None
    recorder_info_address: Optional[str] = None
    recorder_info_email: Optional[str] = None
    recorder_info_phone: Optional[str] = None

    controller_info: Optional[str] = None
    data_source_is_direct_from_subject: Optional[str] = None
    minor_consent_under_10_years: Optional[str] = None
    minor_consent_between_10_to_20_years: Optional[str] = None
    disclosure_without_consent: Optional[str] = None
    dsar_rejection_record: Optional[str] = None

    processor_name: Optional[str] = None
    controller_address: Optional[str] = None
    data_source_is_direct_from_controller: Optional[str] = None
    data_source_indirect_source_detail: Optional[str] = None

    cross_border_transfer_is_transferred: Optional[str] = None
    cross_border_transfer_is_intra_group: Optional[str] = None
    cross_border_transfer_transfer_method: Optional[str] = None
    cross_border_transfer_destination_standard: Optional[str] = None
    cross_border_transfer_section_28_exception: Optional[str] = None

    retention_policy_storage_format: Optional[str] = None
    retention_policy_storage_method: Optional[str] = None
    retention_policy_retention_period: Optional[str] = None
    retention_policy_access_rights_and_methods: Optional[str] = None
    retention_policy_destruction_method: Optional[str] = None

    security_measures_organizational_measure: Optional[str] = None
    security_measures_technical_measure: Optional[str] = None
    security_measures_physical_measure: Optional[str] = None
    security_measures_access_control: Optional[str] = None
    security_measures_user_responsibility: Optional[str] = None
    security_measures_audit_trail: Optional[str] = None

class RopaResponse(RopaSchema):
    id: int
    class Config:
        from_attributes = True