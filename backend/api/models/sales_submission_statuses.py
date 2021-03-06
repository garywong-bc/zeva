from enum import Enum, unique


@unique
class SalesSubmissionStatuses(Enum):
    NEW = 'NEW'
    DRAFT = 'DRAFT'
    SUBMITTED = 'SUBMITTED'
    VALIDATED = 'VALIDATED'
    REJECTED = 'REJECTED'
    RECOMMEND_APPROVAL = 'RECOMMEND_APPROVAL'
    RECOMMEND_REJECTION = 'RECOMMEND_REJECTION'
    DELETED = 'DELETED'
    CHECKED = 'CHECKED'
