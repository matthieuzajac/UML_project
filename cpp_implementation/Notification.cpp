#include "Notification.h"

Notification::Notification(int id, int user_id, const std::string& message,
                           NotificationType type, bool is_read, const std::string& created_at)
    : id(id), user_id(user_id), message(message), type(type),
      is_read(is_read), created_at(created_at) {}

Notification::~Notification() {
}

void Notification::send() {
}

void Notification::markAsRead() {
}
