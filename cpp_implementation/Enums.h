#ifndef ENUMS_H
#define ENUMS_H

enum class NovelStatus {
    DRAFT,
    ACTIVE,
    HIATUS,
    COMPLETED,
    SHADOWBANNED,
    DELETED
};

enum class NotificationType {
    NEW_CHAPTER,
    NEW_REVIEW,
    SYSTEM_MESSAGE,
    MODERATION_ACTION
};

enum class ReadingStatus {
    READING,
    COMPLETED,
    ON_HOLD,
    DROPPED,
    PLAN_TO_READ
};

enum class ReportStatus {
    PENDING,
    REVIEWED,
    RESOLVED,
    DISMISSED
};

#endif
